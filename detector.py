# detector.py

import cv2
import time
import pygame
import os
import numpy as np

class DriverFatigueDetector:
    def __init__(self):
        # Cargar el clasificador de rostros y ojos de Haar Cascade
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        # Cargar el detector de puntos de referencia faciales
        self.landmark_detector = cv2.face.createFacemarkLBF()
        self.landmark_detector.loadModel('assets/lbfmodel.yaml')
        # Establecer el umbral de tiempo para la somnolencia
        self.drowsy_threshold = 2.3
        self.drowsy_start_time = None
        # Inicializar el mezclador de pygame para reproducir sonidos
        pygame.mixer.init()
        self.sound_playing = False
        # Umbral para el ratio de aspecto del ojo (EAR)
        self.EAR_THRESHOLD = 0.25

    def eye_aspect_ratio(self, eye):
        # Calcular las distancias entre los puntos verticales del ojo
        A = np.linalg.norm(eye[1] - eye[5])
        B = np.linalg.norm(eye[2] - eye[4])
        # Calcular la distancia entre los puntos horizontales del ojo
        C = np.linalg.norm(eye[0] - eye[3])
        # Calcular el ratio de aspecto del ojo (EAR)
        ear = (A + B) / (2.0 * C)
        return ear

    def detect_fatigue(self, frame):
        # Convertir el frame a escala de grises
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detectar rostros en el frame
        faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        drowsy_detected = False
        for (x, y, w, h) in faces:
            # Dibujar un rectángulo alrededor del rostro detectado
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            face_roi = gray_frame[y:y+h, x:x+w]
            # Detectar puntos de referencia faciales dentro del rostro
            _, landmarks = self.landmark_detector.fit(gray_frame, np.array([[(x, y, x+w, y+h)]]))
            if len(landmarks) > 0:
                for landmark in landmarks:
                    # Extraer puntos de referencia de los ojos izquierdo y derecho
                    left_eye = landmark[0][36:42]
                    right_eye = landmark[0][42:48]
                    # Calcular el EAR para ambos ojos
                    left_ear = self.eye_aspect_ratio(left_eye)
                    right_ear = self.eye_aspect_ratio(right_eye)
                    ear = (left_ear + right_ear) / 2.0

                    # Verificar si el EAR está por debajo del umbral
                    if ear < self.EAR_THRESHOLD:
                        if self.drowsy_start_time is None:
                            self.drowsy_start_time = time.time()
                        elif time.time() - self.drowsy_start_time >= self.drowsy_threshold:
                            drowsy_detected = True
                            if not self.sound_playing:
                                # Reproducir sonido de alerta si no se está reproduciendo ya
                                alert_sound = pygame.mixer.Sound('assets/Alerta.mp3')
                                alert_sound.play()
                                self.sound_playing = True
                    else:
                        self.drowsy_start_time = None
                        self.sound_playing = False
                    # Dibujar puntos de referencia en los ojos
                    for (lx, ly) in left_eye:
                        cv2.circle(frame, (int(lx), int(ly)), 2, (0, 255, 0), -1)
                    for (rx, ry) in right_eye:
                        cv2.circle(frame, (int(rx), int(ry)), 2, (0, 255, 0), -1)
            else:
                self.drowsy_start_time = None
                self.sound_playing = False
        return frame, drowsy_detected

