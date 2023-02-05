# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 17:51:57 2022

@author: suruj
"""

from PIL import Image
import matplotlib.pyplot as plt
pil = Image.open(r"C:\Users\suruj\Spyder\pht\ocean.jfif")
print(type(pil))
print(pil.size)

largeimg = pil.resize((400, 300))
print(largeimg.size)

largeimg.save(r"C:\Users\suruj\Spyder\resize")
#plt.imshow(pil)
#plt.imshow(largeimg)