# Índices de los landmarks que vamos a usar (ver tabla de MediaPipe Hands)
INDEX_TIP, INDEX_PIP = 8, 6
MIDDLE_TIP, MIDDLE_PIP = 12, 10
RING_TIP, RING_PIP = 16, 14
PINKY_TIP, PINKY_PIP = 20, 18

import mediapipe as mp

#Funcion que devuelve la posicón de un dedo
def finger_extended(hand_landmarks, i):
    tip_y = hand_landmarks.landmark[i+2].y
    pip_y = hand_landmarks.landmark[i].y
    return tip_y < pip_y

#Lista de boleanos, si está extendido es True de lo contrario es False [indice, medio, anular meñique]
def fingers_posicion(hand_landmarks): 
    return [finger_extended(hand_landmarks, i) for i in range(6, 19, 4)]

#Funcion si es un puño
def is_fist(hand_landmarks):
    state_fingers = fingers_posicion(hand_landmarks)
    return not any(state_fingers)

#Funcion si el gesto requerido es correcto
def gesture_selected(all_handlandmarks):
    if all_handlandmarks is None: 
        return False

    for hand_landmarks in all_handlandmarks:
        if is_fist(hand_landmarks):
            return True
    return False
