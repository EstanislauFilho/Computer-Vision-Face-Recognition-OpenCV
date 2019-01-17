'''
Autor: Estanislau de Sena Filho
Projeto: Reconhecimento Facial
'''


import cv2
import os
import numpy as np

eingenface = cv2.face.EigenFaceRecognizer_create(num_components=50)
fisherface = cv2.face.FisherFaceRecognizer_create(num_components=50)
lbph = cv2.face.LBPHFaceRecognizer_create()
print("ok")


def getImage():
    faces_path = [os.path.join('Faces_capturadas/',f) for f in os.listdir('Faces_capturadas/')]
    faces = []
    ids = []

    for i in faces_path:
        image_face = cv2.cvtColor(cv2.imread(i), cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(i)[-1].split('.')[1])
        ids.append(id)
        faces.append(image_face)
        print(id)
    return np.array(ids), faces


ids, faces = getImage()