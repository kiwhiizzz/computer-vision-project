import cv2 as cv
import mediapipe as mp

def get_frame(cap):
    #Lee los fotogramas
    ret, frame = cap.read()
    
    #Warning si no lee los fotogramas
    if not ret:
        print("No se recibio el frame, saliendo...")
        return None

    return frame

def start_cam():
    #Inicializamos la cámara
    cap = cv.VideoCapture(0)

    #Warning por no poder abrir la cámara
    if not cap.isOpened():
        print("No se puede abrir la cámara")
        exit()

    return cap

def start_hands():
    #Inicializar condiciones de las manos
    mp_hands =  mp.solutions.hands
    hands =  mp_hands.Hands(
        min_detection_confidence = 0.5, 
        min_tracking_confidence = 0.5,
        max_num_hands = 2)
    return hands

def landmarks_view(hands, frame) :
    #Trabajando con las manos
    mp_hands =  mp.solutions.hands

    #Iniciamos puntos y landmarks
    mp_drawing = mp.solutions.drawing_utils

            
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    return frame

def main():
    #Inicializamos la cámara
    cap = start_cam()

    #Inicializamos las manos
    hands = start_hands()

    while True:
        #Obtención de frame
        frame = get_frame(cap)
        if frame is None:
            break

        #Muestra los frames
        frame = cv.flip(frame, 1)
        frame = landmarks_view(hands, frame)

        #Muestra la cámara
        cv.imshow('Camera', frame)

        #Comando de finalizar acción / se finaliza con "esc"
        t = cv.waitKey(1)
        if t == 27:
            break

    #Cierra los procesos inicializados en openCV
    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()