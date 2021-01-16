import matplotlib.pyplot as plt
import pydicom
import glob

import cv2
import numpy as np

plt.show()

#читаем dicom файл, проебразуем 

filenames = glob.glob('1010_brain_mr_04_lee/*')
imgs = []

for file in filenames: 
    img = pydicom.dcmread(file).pixel_array.astype(float)
    img_2d_scaled = np.uint8((np.maximum(img,0) / img.max()) * 255.0)
    imgs.append(img_2d_scaled)
    
#image blending
for i in range(len(imgs)-1):
    img1 = imgs[i]
    img2 = imgs[i+1]

    dst = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
    #plt.imshow(dst)
    #plt.show()
    
# Складываем первое и последнее изображение
img1 = imgs[0]
img2 = imgs[-1]

dst = cv2.addWeighted(img1, 0.2, img2, 0.8, 0)
plt.figure(figsize = (10,5))
plt.imshow(dst)
plt.show()

mim1 = cv2.imread('IMG_17.jpg',0)
mim2 = cv2.imread('lung.jpg',0)

mim2 = cv2.resize(mim2, (mim1.shape[1], mim1.shape[0]))
dst = cv2.addWeighted(mim1, 0.2, mim2, 0.8, 0)
plt.figure(figsize = (10,5))
plt.imshow(dst)
plt.show()

# Задание:  проделать операцию cv2.add() для любых 2х изображений