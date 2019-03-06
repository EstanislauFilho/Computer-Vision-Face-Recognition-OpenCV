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

    faces_on_video = face_detect.detectMultiScale(image_video_gray, scaleFactor=1.5, minSize=(100, 100))

    for (x, y, width, heigth) in faces_on_video:
        image_Face = cv2.resize(image_video_gray[y:y + heigth, x:x + width], (width_face, heigth_face))
        cv2.rectangle(image_video, (x, y), (x + width, y + heigth), (0, 255, 0), 2)

        cv2.putText(image_video, name, (x, y + (heigth + 30)), font, 2, (0, 0, 255))

    cv2.imshow("Face Recognizer - Eigenfaces.", image_video)
    cv2.waitKey(1)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break