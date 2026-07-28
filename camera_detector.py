import numpy as np
import cv2 as cv
def main():
    #Inicializamos la cámara
    cap = cv.VideoCapture(0)
    #Warning por no poder abrir la cámara
    if not cap.isOpened():
        print("No se puede abrir la cámara")
        exit()
    #Abrir la cámara
    while True:
        #Lee los fotogramas
        ret, frame = cap.read()
        #Warning si no lee los fotogramas
        if not ret:
            print("No se recibio el frame, saliendo...")
            break

        #Muestra la cámara
        frame = cv.flip(frame, 1)
        cv.imshow('frame', frame)

        #Comando de finalizar acción / se finaliza con "esc"
        t = cv.waitKey(1)
        if t == 27:
            break

    #Descripcion en proceso...
    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()