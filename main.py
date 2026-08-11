import cv2 as cv
from camera_detector import get_frame, start_cam, start_hands,landmarks_view
from gesture_analysis import gesture_selected
from funny_reaction import funny_video
import os

def main():
    #Inicializamos la cámara
    cap = start_cam()

    #Inicializamos las manos
    hands = start_hands()

    reaction = funny_video("assets/funnyReaction.mp4")

    while True:
        #Obtención de frame
        frame = get_frame(cap)
        if frame is None:
            break

        #Muestra los frames
        frame = cv.flip(frame, 1)
        frame, all_hand_landmarks = landmarks_view(hands, frame)

        #Muestra la cámara
        cv.imshow('Camera', frame)

        #Reacciona al recibir cierta acción
        if gesture_selected(all_hand_landmarks):
            if not reaction.playing:
                reaction.start()

        reaction.update()

        #Comando de finalizar acción / se finaliza con "esc"
        t = cv.waitKey(1)
        if t == 27:
            break

    #Cierra los procesos inicializados en openCV
    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()

