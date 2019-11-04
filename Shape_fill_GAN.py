from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from numpy import load
from numpy import expand_dims
import cv2
import matplotlib.pyplot as ptl
import numpy as np


def load_image(filename, size=(256,256)):
	# load image with the preferred size
	pixels = load_img(filename, target_size=size)
	# convert to numpy array
	pixels = img_to_array(pixels)
	# scale from [0,255] to [-1,1]
	pixels = (pixels - 127.5) / 127.5
	# reshape to 1 sample
	pixels = expand_dims(pixels, 0)
	return pixels


##def model_output(img_path):
##    model = load_model('model_009020.h5')
##    img = cv2.resize(img,(256,256,3),interpolation = cv2.INTER_AREA)
##    img = (img-127.5)/127.5
##    img = load_image(img_path)
##    #cv2.imshow('Down-sized',img)
##    filled = model.predict(img)
##    return filled
##
##def plot_images(img,filled):
##    Height,Width = img.shape[:2]
##    orig_dim = [Height,Width]
##    Resized_Fill = cv2.resize(filled,orig_dim,interpolation = cv2.INTER_CUBIC)
##    Images = np.vstack(img,filled,Resized_Fill)
##    Images = (Images + 1)/2.00
##    titles = ['Original','Filled','Resized_Fill']
##
##    for i in range(len(Images)):
##        ptl.subplot(1,3,1+i)
##        ptl.axis('off')
##        ptl.imshow(Images[i])
##        ptl.title(titles[i])
##
##    ptl.show()


def shape_fill():
    #img_path = input("Enter Image Name: ")+'.jpeg'
    img_path = 'Test_Design.jpeg'
    img1 = cv2.imread(img_path,1)
    cv2.imshow('Original',img1)
    model = load_model('model_009020.h5')
    img = load_image(img_path)
    filled = model.predict(img)
    filled = (filled+1)/2.0
    res = filled[0]
    Height,Width = img1.shape[:2]
    orig_dim = (Width,Height)
    Resized_Fill = cv2.resize(res,orig_dim,interpolation = cv2.INTER_CUBIC)
    cv2.imshow('Resized_Fill',Resized_Fill)
    ptl.imshow(filled[0])
    ptl.axis('off')
    ptl.show()
    #plot_images(img,filled)
    

shape_fill()

