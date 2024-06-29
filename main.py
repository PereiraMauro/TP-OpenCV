# main.py

import cv2
from detector import DriverFatigueDetector
from camera import Camera

def main():
    detector = DriverFatigueDetector()
    camera = Camera()

    try:
        while True:
            # Obtener el frame de la cámara
            frame = camera.get_frame()
            # Detectar fatiga en el frame
            frame, drowsy_detected = detector.detect_fatigue(frame)
            if drowsy_detected:
                # Mostrar un mensaje de advertencia en el frame
                cv2.putText(frame, 'CUIDADO', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 6)
            # Mostrar el frame con la detección
            cv2.imshow('Driver Fatigue Detector', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # Liberar la cámara y cerrar todas las ventanas
        camera.release()

if __name__ == '__main__':
    main()

