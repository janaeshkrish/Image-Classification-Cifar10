# Image_classification_cifar10
## Overview
The CIFAR-10 dataset contains 60,000 color images of 32 x 32 pixels in 3 channels divided into 10 classes. Each class contains 6,000 images. The training set contains 50,000 images, while the test sets provides 10,000 images. This image taken from the CIFAR repository ( https://www.cs.toronto.edu/~kriz/cifar.html ). This is a classification problem with 10 classes(muti-label classification). We can take a view on this image for more comprehension of the dataset.

![Test Image 3](/cifar10.png)

- User can select and add a image under the TEN categories  the model will classify the image using graphical user interface.

## Dependencies
- tensorflow 2.0 or higher
- tkinter
- keras
- numpy
- google colab(IDE)

## Usage
Once the dependencies are installed and the model is trained save the model in .h5 format in the current directory.Then run this command

>python widget_for_cifar10.py

It's serving a saved keras model via GUI interface.
![image](/outputs.gif)
