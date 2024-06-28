# detector.py

import cv2
import time
import pygame
import os
import numpy as np

class DriverFatigueDetector:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.landmark_detector = cv2.face.createFacemarkLBF()
        self.landmark_detector.loadModel('assents/lbfmodel.yaml')
        self.drowsy_threshold = 5  # seconds
        self.drowsy_start_time = None
        pygame.mixer.init()  # Initialize the mixer for pygame
        self.sound_playing = False

    def detect_fatigue(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        drowsy_detected = False
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            face_roi = gray_frame[y:y+h, x:x+w]
            _, landmarks = self.landmark_detector.fit(gray_frame, np.array([[(x, y, x+w, y+h)]]))
            for landmark in landmarks:
                for (lx, ly) in landmark[0][36:48]:  # Eye landmarks are points 36-47
                    lx = int(lx)
                    ly = int(ly)
                    cv2.circle(frame, (lx, ly), 2, (0, 255, 0), -1)
            if len(landmarks) == 0:
                if self.drowsy_start_time is None:
                    self.drowsy_start_time = time.time()
                elif time.time() - self.drowsy_start_time >= self.drowsy_threshold:
                    drowsy_detected = True
                    if not self.sound_playing:
                        alert_sound = pygame.mixer.Sound('assents/Alerta.mp3')
                        alert_sound.play()
                        self.sound_playing = True
            else:
                self.drowsy_start_time = None
                self.sound_playing = False
        return frame, drowsy_detected

    