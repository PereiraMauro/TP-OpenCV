import cv2

class DetectorRostro:
    def __init__(self):
        # Carga el clasificador Haar Cascade preentrenado para la detección de rostros
        self._cascade_rostro = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def detectar_rostros(self, cuadro_gris):
        # Detecta caras en la imagen en escala de grises
        rostros = self._cascade_rostro.detectMultiScale(cuadro_gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        return rostros
    
    def get_cascade_rostro(self):
        return self._cascade_rostro