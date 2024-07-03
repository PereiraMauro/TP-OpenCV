import cv2
from detector import DetectorFatiga

class AplicacionDeteccionFatiga:
    def __init__(self):
        # Inicializa el detector de fatiga
        self.detector = DetectorFatiga()
        # Inicia la captura de video
        self.cap = cv2.VideoCapture(0)

    def ejecutar(self):
        while True:
            ret, cuadro = self.cap.read()
            if not ret:
                break

            # Detecta fatiga en el cuadro actual
            cuadro, fatiga_detectada = self.detector.detectar_fatiga(cuadro)

            # Mostrar el cuadro
            cv2.imshow('Deteccion de Fatiga', cuadro)

            # Activa una alerta si se detecta fatiga
            if fatiga_detectada:
                print("Cansancio detectado!! Los ojos se están cerrando.")

            # Romper el bucle si se presiona 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Liberar la captura y cerrar las ventanas
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    app = AplicacionDeteccionFatiga()
    app.ejecutar()
