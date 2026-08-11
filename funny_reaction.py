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
        self.playing = True

    #Como reaacciona despues de terminar el video
    def update(self):
        if not self.playing:
            return
        
        video_frame = get_frame(self.cap)

        if video_frame is None:
            self.stop()
            return
        
        cv.imshow('Funny', video_frame)
    #Detiene el video
    def stop(self): 
        self.cap.release()
        cv.destroyAllWindows('Funny')
        self.playing = False