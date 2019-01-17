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

    print("ok")

