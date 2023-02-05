# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 18:34:34 2022

@author: suruj
"""

from skimage import io
from matplotlib import  pyplot  as plt
from skimage.filters import roberts , sobel , scharr , prewitt
img = io.imread(r"C:\Users\suruj\.spyder-py3\photo-folder\lady.jfif")

'''
from skimage.transform import rescale, resize, downscale_local_mean

img = io.imread(r"C:\Users\suruj\.spyder-py3\photo-folder\lady.jfif")
print(img.size)

rescaled_img = rescale(img , 1.0/4.0 , anti_aliasing = True)
plt.imshow(img)
plt.imshow(rescaled_img)
resize_img = resize(img  , (200, 300))
plt.imshow(resize_img)
image_downscaled = downscale_local_mean(img, (4, 3))
plt.imshow(image_downscaled)

'''



