'''
Autor: Estanislau de Sena Filho
Projeto: Reconhecimento Facial
'''

import cv2
import numpy as np

face_detect = cv2.CascadeClassifier("Classificador/haarcascade_frontalface_default.xml")
eye_detect = cv2.CascadeClassifier("Classificador/haarcascade-eye.xml")

video = cv2.VideoCapture(0)

cont_photo = 1
total_photos = 50

width_face, heigth_face = 250, 250

name = input("Informe seu nome ou um apelido: ")

print("Iniciando Captura de Fotos...")

while(True):
    conect, image_video = video.read()

    image_video_gray = cv2.cvtColor(image_video, cv2.COLOR_BGR2GRAY)

    faces_on_video = face_detect.detectMultiScale(image_video_gray, scaleFactor=1.5, minSize=(100,100))

    for(x, y, width, heigth) in faces_on_video:
        cv2.rectangle(image_video, (x, y), (x + width, y + heigth), (0, 255, 0), 2)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            image_face = cv2.resize(image_video_gray[y:y + heigth, x:x + width], (width_face, heigth_face))
            cv2.imwrite("Faces_captured/"+str(name) + "." + str(cont_photo) + ".jpg",image_face)
            print(str(cont_photo)+"º foto capturada com sucesso, restam "+str(total_photos-cont_photo)+" fotos para finalização da captura...")
            cont_photo += 1

    cv2.imshow("Capturing photos.", image_video)
    cv2.waitKey(1)

    if (cv2.waitKey(1) & 0xFF == ord('q')) or (cont_photo >= total_photos + 1):
        break

print("Fotos capturadas com sucesso!")
video.release()
cv2.destroyAllWindows()