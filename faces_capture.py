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

    image_video_gray = cv2.cvtColor(image_video, cv2.COLOR_BGR2GRAY)

    faces_on_video = face_detect.detectMultiScale(image_video_gray)

    for(x, y, width, heigth) in faces_on_video:
        cv2.rectangle(image_video, (x, y), (x + width, y + heigth), (0, 255, 0), 2)

    cv2.imshow("Capturing photos.", image_video)
    cv2.waitKey(1)

video.release()
cv2.destroyAllWindows()