# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 16:28:14 2022

@author: suruj
"""

import cv2
import matplotlib.pyplot as plt

#read the img
image_dog = cv2.imread(r"C:\Users\suruj\.spyder-py3\test_files\PHOTOS\dogy.jpg")

image_dog_BGR2RGB = cv2.cvtColor(image_dog , cv2.COLOR_BGR2RGB)

#plt.imshow(image_dog_BGR2RGB)

#Print error if cant detect img

if image_dog is None :
    
    print('Could not read image')
    
#image_line = image_dog_BGR2RGB.copy()

#pointA = (400 , 100) #x1 and y1 

#pointB = (800 , 100) #x1 and y1

#cv2.line(image_line , pointA , pointB , (0 , 0 , 278) , thickness = 5 , lineType = cv2.LINE_AA) # it will only convert the image to rgb and plt it but when you run the model it will appear in BGR mode

#plt.imshow(image_line)

#cv2.imshow("image-line-in-dog-face" , image_line)

#cv2.waitKey(0)

#cv2.destroyAllWindows()

#center_coordinates = (550 , 200)

#radius = 180

#cv2.circle(image_dog_BGR2RGB , center_coordinates , radius , (280 , 0 , 0) , thickness = 8 )

#plt.imshow(image_dog_BGR2RGB)  #it will make a circle in the dog-face 

#cv2.circle(image_dog_BGR2RGB , center_coordinates , radius , (280 , 0 , 0) , thickness = -1 )

#plt.imshow(image_dog_BGR2RGB) # it will make a solid circle against the face of the dog due to thickness set -1

#pointA = (400 , 100)

#pointB = (700 , 300)

#cv2.rectangle(image_dog_BGR2RGB , pointA , pointB , (0 , 0 , 100) , thickness = 8) # (0 , 0 , 100) means color-fame RGB

#cv2.imshow("rectange-face-detect" , image_dog_BGR2RGB)

#cv2.waitKey(0)

#cv2.destroyAllWindows()

#plt.imshow(image_dog_BGR2RGB)






