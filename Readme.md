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

### Running faces_capture.py

This python script will capture photos of the faces of the person being recognized. When executing the script, you must enter your name, and after that, pressing the "c" key, 50 photos of the detected faces will be captured manually. All captured photos are resized to a specific dimension and converted to grayscale, and only then are saved in the Faces_captured folder. To test it just run it by the IDE itself.

Another way to execute the script is via terminal, by the following command:

```
sudo python3 faces_capture.py
```

### Running faces_training.py

This python script is intended for training the photos of the face to be recognized. This script collects all images in the Faces_captured folder and builds yml classifiers using the Eigenfaces, Fisherfaces, and LBPH techniques. These classifiers are saved in the Classifiers folder. To test it just run it by the IDE itself.


Another way to execute the script is via terminal, by the following command:

```
sudo python3 faces_training.py
```


### Running faces_eigenface_recognizer.py

This python script does facial recognition using the Eigenface technique. The haarcascade_eigenface_face_recognition.yml classifier that was generated from the face training is responsible for containing the main characteristics of the face to be recognized. To test it just run it by the IDE itself. 


Another way to execute the script is via terminal, by the following command:

```
sudo python3 faces_eigenface_recognizer.py
```

### Running faces_fisherface_recognizer.py

This python script does facial recognition using the Fisherfaces technique. The haarcascade_fisherface_face_recognition.yml classifier that was generated from the face training is responsible for containing the main characteristics of the face to be recognized. To test it just run it by the IDE itself. 


Another way to execute the script is via terminal, by the following command:

```
sudo python3 faces_fisherface_recognizer.py
```


### Running faces_lbph_recognizer.py

This python script does facial recognition using the LBPH technique.
The haarcascade_lbph_face_recognition.yml classifier that was generated from the face training is responsible for containing the main characteristics of the face to be recognized. To test it just run it by the IDE itself.


Another way to execute the script is via terminal, by the following command:

```
sudo python3 faces_lbph_recognizer.py
```


## Developed with

* [OpenCV](https://opencv.org/) - Computer vision library developed by Intel in 1999;
* [Python Software Foundation](https://maven.apache.org/) - Programming language;
* [PyCharm](https://www.jetbrains.com/pycharm/) - IDE used to develop the scrpts.

## Contributing

Please read Contributing.md for details on the process for submitting pull requests to the developer.

## Version

For available versions, see the tags in this repository. 

## Authors

* **Estanislau de Sena Filho** - *Computer Engineering Student at* [CEFET-MG](http://www.cefetmg.br/)

## License

This is not a licensed project. Its purpose is exclusively for computer vision study and learning.

## Special thanks

* Jones Granatyr e Gabriel Alves


