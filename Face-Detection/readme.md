# Face Detection with _Python_ using _OpenCV_

![Face detection](https://media.giphy.com/media/IsKFVXvVxyeN1aXfgj/giphy.gif)
<br></br>
Face detection is a technique that identifies or locates human faces in digital images. A typical example of face detection occurs when we take photographs through our smartphones, and it instantly detects faces in the picture. Face detection is different from Face recognition. Face detection detects merely the presence of faces in an image while facial recognition involves identifying whose face it is.

## Pre-requisites

- Python
- Numpy
- OpenCV installed

## Overview

Face detection is performed by using classifiers. A classifier is essentially an algorithm that decides whether a given image is positive(face) or negative(not a face). A classifier needs to be trained on thousands of images with and without faces.The classifiers used is:
- Haar Classifier

Haar-like features are digital image features used in object recognition.Haar cascade classifier employs a machine learning approach for visual object detection which is capable of processing images extremely rapidly and achieving high detection rates. 

### Haar Cascade Files 

OpenCV comes with a lot of pre-trained classifiers. For instance, there are classifiers for smile, eyes, face, etc. These come in the form of xml files and are located in the opencv/data/haarcascades/ folder. 
However, to make things simple, you can also access them from [here](https://github.com/parulnith/Face-Detection-in-Python-using-OpenCV/tree/master/data/haarcascades).

## Adding the classifier file for frontal face

`face_cascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')`


##  Image path to be tested

`img=cv.imread('love.jpeg')` <br></br>
`gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)`

## Generalized Function 

`faces=face_cascade.detectMultiScale(gray,1.1,4)`

`for (x,y,w,h) in faces:`

  `cv.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)`
  
  
  

