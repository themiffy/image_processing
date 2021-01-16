import matplotlib.pyplot as plt
import pydicom
import glob
import os
import cv2
import numpy as np

import random

def showimage (image,size):
    width = int(image.shape[1] * size / 100)
    height = int(image.shape[0] * size / 100)
    dim = (width, height)
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("Output",image)
    cv2.waitKey(0)

random.seed(version=2)

image_path= "opncv.jpg"

print ('Path exists = ')
print (os.path.exists(image_path))

image = cv2.imread(image_path,1)

print(image)

scale_percent = 100 # Размер изображения в процентах для обработки

width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

#image = cv2.blur(image,(7,7))
img = cv2.bilateralFilter(image,9,0,300)

contours, hierarchy = cv2.findContours( img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours( img, contours, -1, (255,55,30), 3, cv2.LINE_AA, hierarchy, 1 )
showimage(img,100)

'''Задание: 
- Взять изображение здесь: "https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html#median-filtering"
(в пункте "3. Median Filtering", под подписью "original")
- Найти на нем все контуры. 
- Применить к изображению сглаживание ядром 7х7. Найти на полученном изображении все контуры. 
- Сравнить контуры, полученные на изначальном изображении и сглаженном. '''