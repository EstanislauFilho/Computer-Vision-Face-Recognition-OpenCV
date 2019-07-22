# Facial Recognition with OpenCV and Python.

The goal of this project is to create classifiers and python scripts that can perform facial recognition of faces in video streaming. For the development of this project, the OpenCV library and the Python programming language were used.

![alt text](https://raw.githubusercontent.com/EstanislauFilho/Computer-Vision-Face-Recognition-OpenCV/master/Imagens/Resultado.png)


## Starting the Project

The following instructions will allow you to run, develop and contribute to the project in question. Follow all the steps below to run the Facial Recognition project using the OpenCV library and the Python programming language.

### Prerequisites

To run the Python scripts in this project, you need to install the following components on your machine:

```
Python 3.0 ou superior.

IDE de sua preferência.

OpenCV+contrib.
```

## Execution and Testing

To run and test the faces_capture.pym scripts faces_treining.py, faces_eigenface_recognizer.py, faces_fisherface_recognizer.py and faces_lbph_recognizer.py, you must open them in your Python development environment.

### Executando o faces_capture.py

Esse script em python irá fazer a captura de fotos das faces da pessoa a ser reconhecida. Ao executar o script, você deve informar seu nome, e após isso, ao pressionar a tecla "c", 50 fotos das faces detectadas serão capturadas manualmente. Todas as fotos capturadas são redimensionadas para uma dimensão específica e convertidas para escala de cinza, e só depois são salvas na pasta Faces_captured. Para testa-lo basta executá-lo pela própria IDE.

Outra forma de executar o script é via terminal, pelo seguinte comando: 

```
sudo python3 faces_capture.py
```

### Executando o faces_training.py

Esse script em python tem como finalidade fazer o treinamento das fotos referentes a face da pessoa a ser reconhecida. Esse script faz a coleta de todas as imagens na pasta Faces_captured e constrói classificadores do tipo yml, utilizando as técnicas Eigenfaces, Fisherfaces e a LBPH. Esse classificadores são salvos na pasta Classificadores. Para testa-lo basta  executá-lo pela própria IDE. 


Outra forma de executar o script é via terminal, pelo seguinte comando:

```
sudo python3 faces_training.py
```


### Executando o faces_eigenface_recognizer.py

Esse script em python faz o reconhecimento facial utilizando a técnica Eigenface. O classificador haarcascade_eigenface_face_recognition.yml que foi gerado a partir do treinamento das faces, é o responsável conter as caracteriscas principais da face a ser reconhecida. Para testa-lo basta  executá-lo pela própria IDE. 


Outra forma de executar o script é via terminal, pelo seguinte comando:

```
sudo python3 faces_eigenface_recognizer.py
```

### Executando o faces_fisherface_recognizer.py

Esse script em python faz o reconhecimento facial utilizando a técnica Fisherfaces. O classificador haarcascade_fisherface_face_recognition.yml que foi gerado a partir do treinamento das faces, é o responsável conter as caracteriscas principais da face a ser reconhecida. Para testá-lo basta executá-lo pela própria IDE. 


Outra forma de executar o script é via terminal, pelo seguinte comando:

```
sudo python3 faces_fisherface_recognizer.py
```


### Executando o faces_lbph_recognizer.py

Esse script em python faz o reconhecimento facial utilizando a técnica LBPH. O classificador haarcascade_lbph_face_recognition.yml que foi gerado a partir do treinamento das faces, é o responsável conter as caracteriscas principais da face a ser reconhecida. Para testá-lo basta executá-lo pela própria IDE. 


Outra forma de executar o script é via terminal, pelo seguinte comando:

```
sudo python3 faces_lbph_recognizer.py
```


## Desenvolvido com

* [OpenCV](https://opencv.org/) - Biblioteca de visão computacional desenvolvidade pela Intel em 1999;
* [Python Software Foundation](https://maven.apache.org/) - LIguagem programação;
* [PyCharm](https://www.jetbrains.com/pycharm/) - IDE utilizada para desenvolvimento dos scrpts.

## Contribuindo

Por favor, leia Contributing.md para detalhes sobre o processo para enviar pedidos de pull para o desenvolvedor.

## Versão

Para as versões disponíveis, consulte as tags neste repositório. 

## Autores

* **Estanislau de Sena Filho** - *Computer Engineering Student at* [CEFET-MG](http://www.cefetmg.br/)

## Licença

Este não é um projeto licenciado. Sua finalidade é única excluisiva para estudo e aprendizagem sobre visão computacional.

## Agradecimentos

* Jones Granatyr e Gabriel Alves


