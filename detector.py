# detector.py

import cv2
import time
from playsound import playsound

class DriverFatigueDetector:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        self.drowsy_threshold = 5  # seconds
        self.drowsy_start_time = None

    def detect_fatigue(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)
        drowsy_detected = False
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            face_roi = gray_frame[y:y+h, x:x+w]
            eyes = self.eye_cascade.detectMultiScale(face_roi)
            if len(eyes) == 0:
                if self.drowsy_start_time is None:
                    self.drowsy_start_time = time.time()
                elif time.time() - self.drowsy_start_time >= self.drowsy_threshold:
                    drowsy_detected = True
                    playsound('assets/alerta.mp3')
            else:
                self.drowsy_start_time = None
        return frame, drowsy_detected