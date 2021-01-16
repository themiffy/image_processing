import matplotlib.pyplot as plt
import pydicom
import glob

import cv2
import numpy as np

#читаем dicom файл, преобразуем 
def dcm_to_img(filenames):
    dataset = pydicom.dcmread(filenames)
    img = dataset.pixel_array
    img_2d = img.astype(float)
    img_2d_scaled = (np.maximum(img_2d,0) / img_2d.max()) * 255.0
    img_2d_scaled = np.uint8(img_2d_scaled)
    img = img_2d_scaled
    return img

filenames = glob.glob('1010_brain_mr_04_lee/*')

img = dcm_to_img(filenames[0])

min_val = 20 
ret, thresh = cv2.threshold(img, min_val, 255, 0)

contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

areas = []
for i in range(len(contours)):
    areas.append(cv2.contourArea(contours[i]))

max_value = np.where(np.array(areas) == max(areas))

img = cv2.drawContours(img, [contours[max_value[0][0]]],0,(255,0,0),2)

generalMask = np.zeros([img.shape[0], img.shape[1]])
cv2.drawContours(generalMask, [contours[max_value[0][0]]],0,(255,0,0), cv2.FILLED)

for file in filenames: 
    img = dcm_to_img(file)
    min_val = 20 
    ret, thresh = cv2.threshold(img, min_val, 255, 0)
    # находим контуры
    contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    areas = []
    for i in range(len(contours)):
        areas.append(cv2.contourArea(contours[i]))

    max_value = np.where(np.array(areas) == max(areas))

    # рисуем контур
    img = cv2.drawContours(img, [contours[max_value[0][0]]],0,(255,0,0),2)

    # создаем маску
    mask = np.zeros([img.shape[0], img.shape[1]])
    cv2.drawContours(mask, [contours[max_value[0][0]]],0,(255,0,0), cv2.FILLED)
    # применяем маску 
    generalMask = cv2.addWeighted(generalMask,1,mask,1,0)
    #generalMask = generalMask*mask
    

plt.figure(figsize = (4,2))
plt.imshow(generalMask, cmap='gray')
plt.show()

def maskTask():
    for file in filenames: 
        img = dcm_to_img(file)
        img = img*generalMask

        plt.figure(figsize = (8,4))
        plt.imshow(img, cmap='gray')
        plt.show()

#maskTask()

image = cv2.imread('IMG_17.jpg',0)
image = cv2.blur(image, (100,100),cv2.BORDER_DEFAULT)
plt.imshow(image, cmap='gray')
plt.show()
cv2.waitKey(0)
# задание: создать одну маску для всех снимков мозга