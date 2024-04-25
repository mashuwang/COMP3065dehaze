import numpy as np
import cv2


def compare_psnr(img1, img2, maxvalue):
    img1, img2 = img1.astype(np.float64), img2.astype(np.float64)
    mse = np.mean((img1 - img2) ** 2)
    return 10 * np.log10((maxvalue ** 2) / mse)




img2 = cv2.imread('/Users/mashuwang/Desktop/dehaze/ChaIR/Dehazing/ITS/reside-indoor/test/hazy/1401_10.png')
img1 = cv2.imread('/Users/mashuwang/Downloads/test/1401_10.png')
print(compare_psnr(img1, img2, 255))