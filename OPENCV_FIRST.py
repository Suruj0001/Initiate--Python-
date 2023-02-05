# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 10:30:54 2022

@author: suruj
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

# resisizing image

image_amoeba = cv2.imread(r"C:\Users\suruj\.spyder-py3\test_files\PHOTOS\amoeba.jfif")

#plt.imshow(image_amoeba)



# lets downscale an image

down_width = 400

down_height = 300

down_points = (400 , 300)

resize_image_amoeba_down_scale = cv2.resize(image_amoeba , down_points , interpolation = cv2.INTER_LINEAR)

# lets upscale an image

up_width = 800

up_height = 600

up_points = (600 , 600)

resize_image_amoeba_upscale = cv2.resize(image_amoeba , up_points , interpolation = cv2.INTER_LINEAR )

plt.imshow(resize_image_amoeba_down_scale)

plt.imshow("resize_image_amoeba_upscale")

cv2.imshow("rescale_image_amoeba" ,  resize_image_amoeba_upscale)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite(r"C:\Users\suruj\.spyder-py3\test_files\test_PHOTOS_manipulating\rescale_image_amoeba_upscale.jpg" , image_amoeba)


cv2.imwrite(r"C:\Users\suruj\.spyder-py3\test_files\test_PHOTOS_manipulating\rescale_img_amoeba_downscale.jpg" , image_amoeba )


## Resizing with a scalar factor 

scale_up_x = 1.2

scale_up_y = 1.2

scale_down = 0.6

scale_down_image_amoeba = cv2.resize(image_amoeba , None , fx = scale_down , fy = scale_down , interpolation = cv2.INTER_LINEAR)

scale_up_image_amoeba = cv2.resize(image_amoeba , None , fx = scale_up_x , fy = scale_up_y , interpolation = cv2.INTER_LINEAR)

plt.imshow(scale_down_image_amoeba)

plt.imshow(scale_up_image_amoeba)




















