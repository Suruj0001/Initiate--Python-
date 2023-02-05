# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 19:22:36 2022

@author: suruj
"""

from skimage import io , restoration 
from matplotlib import  pyplot  as plt
from skimage.filters import roberts , sobel , scharr , prewitt , try_all_threshold , threshold_otsu
import numpy as np
from skimage.feature import canny
from skimage.filters.rank import entropy
from skimage.morphology import disk

bacteria_img = io.imread(r"C:\Users\suruj\.spyder-py3\photo-folder\amoeba.jfif" , as_gray=True)
plt.imshow(bacteria_img)

entropy_img = entropy(bacteria_img , disk(3) )
plt.imshow(entropy_img , cmap='gray')

fig , ax = try_all_threshold(entropy_img , figsize = (10,8) , verbose=False)

thresh = threshold_otsu(entropy_img)

binary = entropy_img <= thresh
plt.imshow(binary , cmap=True)

