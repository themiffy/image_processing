import cv2
import random

def showimage (image,size):
    width = int(image.shape[1] * size / 100)
    height = int(image.shape[0] * size / 100)
    dim = (width, height)
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("Output",image)
    cv2.waitKey(0)

random.seed(version=2)

image = cv2.imread('lung.jpg',0)

scale_percent = 100 # Размер изображения в процентах для обработки

width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

# searching for contours on rough image
img = cv2.Canny(image, 100, 200)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

contours, hierarchy = cv2.findContours( img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours( img, contours, -1, (255,55,30), 3, cv2.LINE_AA, hierarchy, 1 )
showimage(img,100)

img = cv2.blur(image,(7,7))
#img = cv2.bilateralFilter(image,9,0,300)

img = cv2.Canny(img, 100, 200)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

contours, hierarchy = cv2.findContours( img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours( img, contours, -1, (255,55,30), 3, cv2.LINE_AA, hierarchy, 1 )
showimage(img,100)