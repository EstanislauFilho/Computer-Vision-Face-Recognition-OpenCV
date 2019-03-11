# Reconhecimento Facial com OpenCV e Python

Este projeto conciste na criação de classificadores e scripts em python, que possam realizar o reconhecimento facial de faces em streaming por meio de uma Webcam. Para desenvolvimento deste projeto utilizou-se a biblioteca OpenCV e a linguagem de programação Python.

![alt text](https://raw.githubusercontent.com/EstanislauFilho/Computer-Vision-Face-Recognition-OpenCV/master/Imagens/Resultado.png)


## Iniciando o Projeto

As instruções a seguir permitirá que você possa executar, desenvolver e contribuir para o projeto em questão. Siga todas as etapas abaixo para executar o projeto de Reconhecimento Facial utilizando a biblioteca OpenCV e a linguagem de programação Python.

### Pré-requisitos

Para executar os scripts em Python presentes nesse projeto, você precisa instalar em sua máquina os seguintes componentes:

```
Python 3.0 ou superior.

IDE de sua preferência.

OpenCV+contrib.
```

## Execução e Testes

Para executar e testar os scripts face_detect_image.py e face_detect_webcam.py, você inicialmente deve abri-los em seu ambiente de desenvolvimento em Python.

### Executando o faces_capture.py

Esse script em python irá fazer a captura de fotos das faces da pessoa a ser reconhecida. Ao executar o script, você deve informar seu nome, e após isso, ao pressionar a tecla "c", 50 fotos das faces detectadas serão capturadas manualmente. Todas as fotos capturadas são redimensionadas para uma dimensão específica e convertidas para escala de cinza, e só depois são salvas na pasta Faces_captured. Para testa-lo basta executá-lo pela própria IDE.

Outra forma de executar o script é via terminal, pelo seguinte comando: 

```
sudo python3 face_detect_image.py
```

### Executando o face_detect_webcam.py

Esse script em python tem como finalidade fazer a detecção facial em streming através de uma webcam. Para testa-lo basta  executá-lo pela própria IDE. 


Outra forma de executar o script é via terminal, pelo seguinte comando:

```
sudo python3 face_detect_webcam.py
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


