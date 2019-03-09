'''
Autor: Estanislau de Sena Filho
Projeto: Reconhecimento Facial
'''


import cv2
import os
import numpy as np

eigenface = cv2.face.EigenFaceRecognizer_create(num_components=50)
fisherface = cv2.face.FisherFaceRecognizer_create(num_components=50)
lbph = cv2.face.LBPHFaceRecognizer_create()


def getImage():
    faces_path = [os.path.join('Faces_captured/',f) for f in os.listdir('Faces_captured/')]
    faces = []
    ids = []

    for i in faces_path:
        image_face = cv2.cvtColor(cv2.imread(i), cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(i)[-1].split('.')[1])
        ids.append(id)
        faces.append(image_face)
    return np.array(ids), faces


ids, faces = getImage()

print("Iniciando Treinamento...")

eigenface.train(faces, ids)
eigenface.write('Classificador/haarcascade_eigenface_face_recognition.yml')

fisherface.train(faces, ids)
fisherface.write('Classificador/haarcascade_fisherface_face_recognition.yml')

lbph.train(faces, ids)
lbph.write('Classificador/haarcascade_lbph_face_recognition.yml')

print("Treinamento realizado com sucesso!")