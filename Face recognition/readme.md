UAceIt-Winter-of-Mentorship

# FACE RECOGNITION USING LBPH

## *LBPH (Local Binary Patterns Histogram)*
It is a type of visual descriptor used for classification in computer vision.
It is a simple and very efficient texture operator which labels the pixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number.The steps involved to achieve this are:
creating dataset
face acquisition
feature extraction
classification


## *IMAGES*

<p align="center"><img src="https://github.com/Vinamrata1086/Face-X/blob/master/Recognition-Algorithms/Facial%20Recognition%20using%20LBPH/images/pic1.png"><br>
Divide face images into R( for example R = 3 x 3 = 9 Regions) local regions to extract LBP histograms.</p>


<p align="center"><img src="https://github.com/Vinamrata1086/Face-X/blob/master/Recognition-Algorithms/Facial%20Recognition%20using%20LBPH/images/pic2.png" ><br>
Three neighborhood examples used to define a texture and calculate a local binary pattern (LBP).</p>

<p align="center">
    <img src="https://github.com/Vinamrata1086/Face-X/blob/master/Recognition-Algorithms/Facial%20Recognition%20using%20LBPH/images/pic3.png"><br>
    After applying the LBP operation we extract the histograms of each image based on the number of grids (X and Y) passed by parameter. After extracting the histogram of each region, we concatenate all histograms and create a new one which will be used to represent the image.
</p>
    
#
#
### face recognition part 1:
This code collects the 300 pictures through webcam and stores the pictures in the given data path. 

### face recognition part 2:
This code uses the pictures that was collected in face recognition part 1, to recognise the face.

#
#
## Installation
- pip install numpy
- pip install opencv-python
- pip install skimage


## Requirements 
- jupyter lab/ pycharm
- opencv
- haarcascade_frontalface_default.xml file

