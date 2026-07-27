import numpy as np
import cv2 as cv
def main():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("No se puede abrir la cámara")
        exit()
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("No se recibio el fotograma, saliendo...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        cv.imshow('frame', gray)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()