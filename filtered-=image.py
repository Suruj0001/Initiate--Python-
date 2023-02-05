# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 12:26:53 2022

@author: suruj
"""

from skimage import io , img_as_ubyte
import numpy as np
from matplotlib import pyplot as plt 
from scipy import ndimage



#gaussian_filter = ndimage.gaussian_filter(image, sigma=11)
#plt.imshow(gaussian_filter)
image2 = io.imread(r"C:\Users\suruj\.spyder-py3\photo-folder\noisy.jpg")
plt.imshow(image2)
median_filter = ndimage.median_filter(image2 , 3)
plt.imshow(median_filter)


