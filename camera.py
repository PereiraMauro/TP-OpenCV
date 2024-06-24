# camera.py

import cv2

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Failed to capture image")
        return frame

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
