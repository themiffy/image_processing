import matplotlib.pyplot as plt
import pydicom
import glob

import cv2
import numpy as np

#читаем dicom файл, проебразуем 

filenames = glob.glob('1010_brain_mr_04_lee/*')

for file in filenames[:1]: 
    dataset = pydicom.dcmread(file)
    
    img = dataset.pixel_array

    img_2d = img.astype(float)
    #перенормировка
    img_2d_scaled = (np.maximum(img_2d,0) / img_2d.max()) * 255.0
    img_2d_scaled = np.uint8(img_2d_scaled)

img = img_2d_scaled

img
# делаем преобразование фурье 
f = np.fft.fft2(img)
dft_shift = np.fft.fftshift(f)

magnitude_spectrum = 20*np.log(np.abs(dft_shift))

# выводим амплитуду частот в разложении

rows, cols = img.shape[:2]
crow,ccol = rows//2 , cols//2

# создаем маску, которая будет оставлять только медленные частоты
mask = np.zeros((rows,cols),np.uint8)
mask[crow-5:crow+5, ccol-5:ccol+5] = 1

# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.imshow(img_back, cmap = 'gray')
plt.title('low freq'), plt.xticks([]), plt.yticks([])
plt.show()

mask = np.zeros((rows,cols),np.uint8)
mask[crow-40:crow+40, ccol-40:ccol+40] = 1

# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.imshow(img_back, cmap = 'gray')
plt.title('medium freq'), plt.xticks([]), plt.yticks([])
plt.show()

mask = np.zeros((rows,cols),np.uint8)
mask[crow-160:crow+160, ccol-160:ccol+160] = 1

# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.imshow(img_back, cmap = 'gray')
plt.title('high freq'), plt.xticks([]), plt.yticks([])
plt.show()

'''Задание: сделать 3 картинки: Оставив только быстрые частоты, только медленные и средние частоты. '''

