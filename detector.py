import cv2
import dlib
import winsound
from detector_cara import DetectorRostro
from detector_ojos import DetectorOjos, forma_a_np

class DetectorFatiga:
    def __init__(self):
        # Inicializa los detectores de rostro y ojos
        self.detector_rostro = DetectorRostro()
        self.detector_ojos = DetectorOjos()

        # Carga el predictor de puntos faciales
        self.predictor = dlib.shape_predictor("assets/shape_predictor_68_face_landmarks.dat")

        # Umbral EAR y conteo de cuadros consecutivos
        self.UMBRAL_EAR = 0.21
        self.CUADROS_CONSECUTIVOS_EAR = 15

        # Inicializa el contador de cuadros y el booleano de la fatiga
        self.contador = 0
        self.fatiga_detectada = False

    def detectar_fatiga(self, cuadro):
        gris = cv2.cvtColor(cuadro, cv2.COLOR_BGR2GRAY)
        rostros = self.detector_rostro.detectar_rostros(gris)

        for (x, y, w, h) in rostros:
            rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
            forma = self.predictor(gris, rect)
            forma = forma_a_np(forma)

            ojo_izquierdo = forma[36:42]
            ojo_derecho = forma[42:48]

            EAR_izquierdo = self.detector_ojos.calcular_ear(ojo_izquierdo)
            EAR_derecho = self.detector_ojos.calcular_ear(ojo_derecho)

            ear = (EAR_izquierdo + EAR_derecho) / 2.0

            if ear < self.UMBRAL_EAR:
                self.contador += 1

                if self.contador >= self.CUADROS_CONSECUTIVOS_EAR:
                    self.fatiga_detectada = True
                    cv2.putText(cuadro, "¡ALERTA DE CANSANCIO!", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    winsound.Beep(1000, 500)  # Frecuencia, duración en ms
            else:
                self.contador = 0
                self.fatiga_detectada = False

            for (x, y) in ojo_izquierdo:
                cv2.circle(cuadro, (x, y), 1, (0, 255, 0), -1)
            for (x, y) in ojo_derecho:
                cv2.circle(cuadro, (x, y), 1, (0, 255, 0), -1)

        return cuadro, self.fatiga_detectada
