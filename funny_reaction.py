import cv2 as cv
import pygame
from camera_detector import get_frame
#Haremos una clase del video que aparecera
class funny_video:
    def __init__(self, video_path, audio_path):
        self.video_path = video_path
        self.cap = None
        self.playing = False
        self.audio_path = audio_path
        pygame.mixer.init()

    #Como inicializar el video 
    def start(self):
        self.cap = cv.VideoCapture(self.video_path)
        self.playing = True
        pygame.mixer.music.load(self.audio_path)
        pygame.mixer.music.play()

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
        if self.cap is not None:
            self.cap.release()
            pygame.mixer.stop()
        try:
            cv.destroyWindow('Funny')
        except cv.error:
            pass
        self.playing = False