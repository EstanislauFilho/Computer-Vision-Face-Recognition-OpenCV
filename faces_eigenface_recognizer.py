'''
Autor: Estanislau de Sena Filho
Projeto: Reconhecimento Facial
'''

import cv2

face_detect = cv2.CascadeClassifier("Classificador/haarcascade_frontalface_default.xml")

recognizer = cv2.face.EigenFaceRecognizer_create()
#recognizer.read("Classificador/nome.yml")

font = cv2.FONT_HERSHEY_COMPLEX_SMALL

width_face, heigth_face = 220, 220

video = cv2.VideoCapture(0)

name = ''

while(True):
    conect, image_video = video.read()

    image_video_gray = cv2.cvtColor(image_video, cv2.COLOR_BGR2GRAY)

    
