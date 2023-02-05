# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 17:54:26 2022

@author: suruj
"""

import cv2

import numpy as np

import matplotlib.pyplot as plt

image_buggati = cv2.imread(r"C:\Users\suruj\.spyder-py3\test_files\PHOTOS\buggati_veron.jpg")

#cv2.imshow( 'image' , image_buggati )

#cv2.imwrite(r"C:\Users\suruj\.spyder-py3\test_files\PHOTOS\scenery.jpg" , image_buggati)

#cv2.waitKey(0)

#cv2.destroyAllWindows()

#plt.imshow(image_buggati)

downpoints = [1000 , 600]

image_buggati_resize = cv2.resize(image_buggati , downpoints , interpolation = cv2.INTER_LINEAR) 

#resizing the image since we know the first image_buggati exceeds the pixels

#plt.imshow(image_buggati_resize)

height , width = image_buggati_resize.shape[:2] #Getting the height and width of an image in the center 

center = (width/2 , height/2)

rotate_matrix = cv2.getRotationMatrix2D(center=center , angle=45 , scale=1)

rotated_img = cv2.warpAffine(src = image_buggati_resize , M = rotate_matrix , dsize = (width ,height))

#plt.imshow(rotated_img)

image_translate = cv2.imread(r"C:\Users\suruj\.spyder-py3\test_files\PHOTOS\buggati_veron.jpg")

#plt.imshow(image_translate)

height , width = image_translate.shape[:2]

# get tx and ty values for translation
# you can specify any value of your choice

tx, ty = width / 4 , height / 4

translation_matrix = np.array([

    [1, 0, tx],

    [0, 1, ty]

], dtype=np.float32)

translated_img = cv2.warpAffine(src = image_translate , M = translation_matrix , dsize = (width , height) )

#plt.imshow(translated_img)

rgb_tranlate_img = cv2.cvtColor(translated_img , cv2.COLOR_BGR2RGB)

#plt.imshow(rgb_tranlate_img)










