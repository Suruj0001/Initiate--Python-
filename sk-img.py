# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 14:22:04 2022

@author: suruj
"""

from skimage import io , img_as_ubyte
import numpy as np
from matplotlib import pyplot as plt 
from scipy import ndimage
#SciPy is a scientific computation library that uses NumPy underneath.
#SciPy stands for Scientific Python.
img = img_as_ubyte(io.imread(r"C:\Users\suruj\.spyder-py3\photo-folder\suruj.jpg " , as_gray=True))
print(img.dtype , img.shape)
#print(img[10:25 , 20:30])
img2 = io.imread(r"C:\Users\suruj\.spyder-py3\photo-folder\suruj.jpg")
#The io.open() function is a much preferred way to perform I/O operations as
# it is made as a high-level Pythonic interface.
#Since io.open() is a wrapper function to os.open(), it is generally good practice
# to use such wrapper functions, since they automatically handle many errors for you.
arr = np.array(img2)
arr2 = arr.astype(float)
print(arr2.shape , arr2.dtype)
maximg = img.max()
meanimg = img.mean()
minimg = img.min()
print("Max  mean min : " ,  maximg , meanimg , minimg)
img3 = io.imread(r"C:\Users\suruj\.spyder-py3\photo-folder\suruj.jpg")
# If we directly convert a image to np i.e img = np.io.read("//location) then when we call the img.shape it will show ()
#meaning o dimensions anmd in that case flipr = np.flipltr(img) will not work , so first we need to convert it to np at least 2d
# then we can start with it of flipping the image
arr3 = np.array(img3)
print(arr3.dtype , arr3.shape)
flipR = np.fliplr(img3)
flipud = np.flipud(img3)
plt.subplot(1 , 3 , 1)
plt.imshow(img3)
plt.subplot(1 , 3 , 2)
plt.imshow(flipR)
plt.subplot(1 ,3, 3)
plt.imshow(flipud)
#rotate45= img3.rotate(45)
#'numpy.ndarray' object has no attribute 'rotate'
rotated = ndimage.rotate(img3 , 45)
plt.imshow(rotated)
rotated90 = ndimage.rotate(img3 , 90)
plt.imshow(rotated90)

