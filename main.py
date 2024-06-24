# main.py

import cv2
from detector import DriverFatigueDetector
from camera import Camera

def main():
    detector = DriverFatigueDetector()
    camera = Camera()

    try:
        while True:
            frame = camera.get_frame()
            frame, drowsy_detected = detector.detect_fatigue(frame)
            if drowsy_detected:
                cv2.putText(frame, 'Drowsiness Detected!', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Driver Fatigue Detector', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        camera.release()

if __name__ == '__main__':
    main()

