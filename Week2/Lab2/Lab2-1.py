import cv2 as cv
import sys
from matplotlib import pyplot as plt

img = cv.imread('../Lab2 Image/myimage.png')

if img is None:
    sys.exit("파일을 찾을 수 없습니다")

print("Image Size = ", img.shape) # image size [height width channel]
h, w, c = img.shape

print('Pixel Intensity Value = ', img[100, 70]) # access the pixel intensity value at the position of (100, 70)

"""
OpenCv --> BGR image
"""

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

roi = img[50:300, 30:300] # image cropping (ROI extraction by slicing)

cv.imshow('Color Image', img)
cv.imshow('Gray Image', gray)
cv.imshow('Cropped Image', roi)

"""
matplotlib --> RGB image
"""

# RGB_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# RGB_roi = RGB_img[50:400, 30:480]
# roi = img[50:400, 30:480]
# plt.imshow(RGB_roi)
# plt.show()

cv.waitKey()
cv.destroyAllWindows()

