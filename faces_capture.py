'''
Autor: Estanislau de Sena Filho
Projeto: Reconhecimento Facial
'''

import cv2
import numpy as np

face_detect = cv2.CascadeClassifier("Classificador/haarcascade_frontalface_default.xml")
eye_detect = cv2.CascadeClassifier("Classificador/haarcascade-eye.xml")

video = cv2.VideoCapture(0)

cont_foto = 1
total_photos = 50

print("Capturing photos...")

while(True):
    conect, image_video = video.read()
