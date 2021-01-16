import matplotlib.pyplot as plt
import pydicom
import glob

import cv2
import numpy as np

#читаем dicom файл, проебразуем 

filenames = glob.glob('1010_brain_mr_04_lee/*')

for file in filenames: 
    dataset = pydicom.dcmread(file)
    
    img = dataset.pixel_array

    img_2d = img.astype(float)
    #перенормировка
    img_2d_scaled = (np.maximum(img_2d,0) / img_2d.max()) * 255.0
    img_2d_scaled = np.uint8(img_2d_scaled)

#     plt.imshow(img_2d_scaled, cmap='gray', vmin=0, vmax=255)
#     plt.show()

img = img_2d_scaled
# преобразуем в черно-белое
min_val = 20 # попробуйте поменять это значение. На что оно влияет? 
ret, thresh = cv2.threshold(img, min_val, 255, 0)
# находим контуры
contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print('r - for rectangle, e - ellipse')
a = input()
# рисуем контуры
for cnt in contours:
    
#     img = img_2d_scaled.copy()
    #находим прямоугольник, в который входит наш контур
    if a == 'r':
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        #рисуем прямоугольник
        img = cv2.drawContours(img,[box],0,(255,0,0),2)
    elif a == 'e':
        #(x,y),radius = cv2.minEnclosingCircle(cnt)
        #center = (int(x),int(y))
        #radius = int(radius)
        #cv2.circle(img,center,radius,(255,0,0),2)
        ellipse = cv2.minAreaRect(cnt)
        cv2.ellipse(img,ellipse,(255,0,0),2)
    else:
        cv2.drawContours(img, contours, -1, (255,0,0), 3)
    
#     Задание: Нарисовать элипс, квадрат и границы контура
    
plt.figure(figsize = (10,5))
plt.imshow(img, cmap=plt.cm.bone)
plt.show()