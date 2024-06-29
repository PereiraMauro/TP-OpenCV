# camera.py

import cv2

class Camera:
    def __init__(self):
        # Inicializar la captura de video de la cámara
        self.cap = cv2.VideoCapture(0)

    def get_frame(self):
        # Leer un frame de la cámara
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Failed to capture image")
        return frame

    def release(self):
        # Liberar la cámara y cerrar todas las ventanas de OpenCV
        self.cap.release()
        cv2.destroyAllWindows()
