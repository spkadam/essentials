"""
Author: Samruddhi K

For resizing the images and/or converting jpeg/jpg images to png

"""

#importing required libraries
import os, sys
import cv2
import numpy as np
from PIL import Image

#dimensions after resizing
IMAGE_HEIGHT1, IMAGE_WIDTH1, IMAGE_CHANNELS1 = (160, 576, 3) 
def load_image(image_file):
    """
    Load RGB images from a complete filepath (image_file)
    Don't use matplot image
    """
    result = cv2.imread(image_file)
    return result
    
def save_image(image_path_save,img):
    """
    Saves resized RGB images from 'img' to complete filepath (image_path_save)
    Don't use matplot image
    """
    result = cv2.imwrite(image_path_save,img)
    return result
    

for index in range(100):
    image_path = ("/home/sam/Desktop/images/airplane_"+str(index)+".jpg")#image file to crop
    img = load_image(image_path)
    img = cv2.resize(img, (IMAGE_WIDTH1, IMAGE_HEIGHT1))
    image_path_save = ('/home/sam/Desktop/ResizedImages/'+str(index)+'_resized.png')
    img = save_image(image_path_save,img)

