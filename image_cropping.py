# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 18:56:38 2022

@author: suruj
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img_sunflower = cv2.imread(r"C:\Users\suruj\.spyder-py3\test_files\PHOTOS\sunflower.jfif")

convert_img_sunflower_BGR2RGB = cv2.cvtColor(img_sunflower , cv2.COLOR_BGR2RGB)

#plt.imshow(img_sunflower)  # IT WILL SHOW BGR color image

#image_cropped = img_amoeba[5:50 , 50:100]

#plt.imshow(image_cropped)


#plt.imshow(convert_img_sunflower_BGR2RGB)

print(convert_img_sunflower_BGR2RGB.shape)

image_sunflower_rgb_copy = convert_img_sunflower_BGR2RGB.copy()


image_sunflower_rgb_copy_height = image_sunflower_rgb_copy.shape[0]

image_sunflower_rgb_copy_width = image_sunflower_rgb_copy.shape[1]

# Creating rectange patches in the image_sunflower_rgb_copy 

# Creating patches of height and width of size (h = 151/3 = 50 , w = 246/3 = 82) 

w = 82

h = 50

x1 = 0

y1 = 0

for y in range(0 , 151 , h):
    
    for x in range(0 , 246 , w):
        
        if (image_sunflower_rgb_copy_height - y) < h or (image_sunflower_rgb_copy_width - x) < w :
    
                break
            
        x1 = x + w  # travelling through the width  patch
        
        y1 = y1 + h  # travelling through the height patch 
        
        ##Checking whether a patch exceeds the given patch dimensions
        
        if x1 >= image_sunflower_rgb_copy_width and y1 >= image_sunflower_rgb_copy_height :
            
            x1 = image_sunflower_rgb_copy_width - 1 
            
            y1 = image_sunflower_rgb_copy_height - 1
            
            tiles = image_sunflower_rgb_copy[y:y+h , x:x+w]
            
            cv2.imwrite(r"C:\Users\suruj\.spyder-py3\test_files\test_PHOTOS_manipulating\Cropped_sunflower.jpg" , tiles)
            
            cv2.rectangle(img_sunflower , (x , y) , (x1 , y1) , (0 , 255 , 0) , 1)
            
        elif x1 >= image_sunflower_rgb_copy_width : 
            
            x1 = image_sunflower_rgb_copy_width - 1
            
            tiles = image_sunflower_rgb_copy[y:y+h , x:x+w]
            
            cv2.imwrite(r"C:\Users\suruj\.spyder-py3\test_files\test_PHOTOS_manipulating\Cropped_sunflower.jpg" , tiles)
            
            cv2.rectangle(img_sunflower , (x , y) , (x1 , y1) , (0 , 255 , 0) , 1)
            
        elif y1 >= image_sunflower_rgb_copy_height :
            
            y1 = image_sunflower_rgb_copy_height - 1
            
            tiles = image_sunflower_rgb_copy[y:y+h , x:x+w]
            
            cv2.imwrite(r"C:\Users\suruj\.spyder-py3\test_files\test_PHOTOS_manipulating\Cropped_sunflower.jpg" , tiles)
            
            cv2.rectangle(img_sunflower , (x , y) , (x1 , y1) , (0 , 255 , 0) , 1)
            
        else : 
            
            tiles = image_sunflower_rgb_copy[ y:y+h , x:x+w]

            cv2.imwrite(r"C:\Users\suruj\.spyder-py3\test_files\test_PHOTOS_manipulating\Cropped_sunflower.jpg" , tiles)
            
            cv2.rectangle(img_sunflower , (x , y) , (x1 , y1) , (0 , 255 , 0) , 1)
            



            
#plt.imshow(tiles) # it will print the ROI 

#plt.imshow(img_sunflower)  #IT WILL SHOW THE RECTANGLE DRAWN in the image_sunflower in BGR mode
    
cv2.imshow("Patch_img" , img_sunflower )

#cv2.imwrite(r"C:\Users\suruj\.spyder-py3\test_files\test_PHOTOS_manipulating\Cropped_sunflower.jpg" , img_sunflower )

cv2.waitKey(0)

cv2.destroyAllWindows()






            
             




            
            








        
            

        
            
            
        
    
        