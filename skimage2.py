# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 19:42:24 2022

@author: suruj
"""

from skimage import io
from matplotlib import  pyplot  as plt
from skimage.filters import roberts , sobel , scharr , prewitt
import numpy as np
from skimage.feature import canny
from skimage import restoration
from skimage.filters.rank import entropy
from skimage.morphology import disk
img = io.imread(r"C:\Users\suruj\.spyder-py3\photo-folder\lady.jfif")
#plt.imshow(img)
print(img.shape)
img_grey = io.imread(r"C:\Users\suruj\.spyder-py3\photo-folder\lady.jfif" , as_gray=True)
#plt.imshow(img_grey)
print(img_grey.shape)
edge_sobel = sobel(img_grey)
edge_scharr = scharr(img_grey)
edge_robert = roberts(img_grey)
edge_prewitt = prewitt(img_grey)


canny_img = canny(img_grey , sigma=4)
#plt.imshow(canny_img)


psf = np.ones((3,3)) / 13
deconvulation , _  = restoration.unsupervised_wiener(img_grey , psf)
#plt.imshow(deconvulation)
#plt.subplot(121)
#plt.imshow(deconvulation)
'''
plt.subplot(122)
plt.imshow(img_grey)
'''
img_bacteria = io.imread(r"C:\Users\suruj\.spyder-py3\photo-folder\amoeba.jfif")
#plt.imshow(img_bacteria)
entr_img = entropy(img_bacteria, disk(3))
print(img_bacteria.shape)
#plt.imshow(entr_img , cmap='gray')

