import cv2 as cv
import sys
from matplotlib import pyplot as plt
import numpy as np

img = cv.imread('../Lab2 Image/myimage.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

if img is None:
    sys.exit('파일을 찾을 수 없습니다')

# Image Blurring (Image Smoothing) using 2D convolution (Image filtering)

# 1. Averaging

"""
OpenCV --> BGR image
"""

kernel = np.ones((5, 5), np.float32) / 25  # kernel setting
dst = cv.filter2D(img, -1, kernel)  # output image
dst_gray = cv.filter2D(gray, -1, kernel)  # output image
gaussian_gray1 = cv.GaussianBlur(gray, (0, 0), 1)
gaussian_gray3 = cv.GaussianBlur(gray, (0, 0), 3)

cv.imshow('Original Image', img)
cv.imshow('Averaging Image', dst)
cv.imshow('Original Image Gray', gray)
cv.imshow('Averaging Image Gray', dst_gray)
cv.imshow("Gaussian Image Gray with Sigma = 1", gaussian_gray1)
cv.imshow("Gaussian Image Gray with Sigma = 3", gaussian_gray3)


"""
matplotlib --> RGB image
"""

# RGB_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # convert color space from BGR to RGB
# kernel = np.ones((5, 5), np.float32) / 25  # kernel setting
# dst2 = cv.filter2D(RGB_img, -1, kernel)  # output image (opencv is applied)
# dst2_gray = cv.filter2D(gray, -1, kernel)  # output image (opencv is applied)
#
# plt.subplot(121), plt.imshow(RGB_img), plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(dst2), plt.title('Averaging')
# plt.xticks([]), plt.yticks([])
# plt.show()
#
# plt.subplot(121), plt.imshow(gray), plt.title('Original Gray')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(dst2_gray), plt.title('Averaging')
# plt.xticks([]), plt.yticks([])
# plt.show()

cv.waitKey()
cv.destroyAllWindows()
