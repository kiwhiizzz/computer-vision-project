import cv2 as cv
from camera_detector import get_frame
#Haremos una clase del video que aparecera
class funny_video:
    def __init__(self, path):
        self.path = path
        self.cap = None
        self.playing = False

    #Como inicializar el video 
    def start(self):
        self.cap = cv.VideoCapture(self.path)
        video_frame = get_frame(self.cap)
        cv.imshow('Funny', video_frame)

    #Como reaacciona despues de terminar el video
    def update(self):
        pass

    #Detiene el video
    def stop(self):
        pass