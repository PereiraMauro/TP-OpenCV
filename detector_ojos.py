import cv2
import numpy as np
from scipy.spatial import distance as dist

class DetectorOjos:
    def __init__(self):
        # Carga el clasificador Haar Cascade preentrenado para la detección de ojos
        self._cascade_ojos = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    def detectar_ojos(self, cuadro_gris):
        # Detecta ojos en la imagen en escala de grises
        ojos = self._cascade_ojos.detectMultiScale(cuadro_gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        return ojos

    def calcular_ear(self, ojo):
        A = dist.euclidean(ojo[1], ojo[5])
        B = dist.euclidean(ojo[2], ojo[4])
        C = dist.euclidean(ojo[0], ojo[3])
        ear = (A + B) / (2.0 * C)
        return ear

def forma_a_np(forma, dtype="int"):
    coords = np.zeros((68, 2), dtype=dtype)
    for i in range(0, 68):
        coords[i] = (forma.part(i).x, forma.part(i).y)
    return coords
