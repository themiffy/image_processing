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

for file in filenames:
    img = dcm_to_img(file)
    plt.imshow(img, cmap='gray')
    plt.show()
    cv2.waitKey(0)