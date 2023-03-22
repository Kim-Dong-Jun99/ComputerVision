import cv2 as cv
import sys
import matplotlib.pyplot as plt

img = cv.imread('bus.jpg')
if img is None:
    sys.exit("파일을 찾을 수 없습니다")

colors = ['b', 'g', 'r']
bgr_planes = cv.split(img)

for (p, c) in zip(bgr_planes, colors):
    histogram = cv.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(histogram, color=c, linewidth=3)
plt.show()

# hist1 = cv.calcHist([img], [0], None, [256], [0, 256])
# hist2 = cv.calcHist([img], [1], None, [256], [0, 256])
# hist3 = cv.calcHist([img], [2], None, [256], [0, 256])
#
# plt.subplot(221), plt.plot(hist1, color='b'),
# plt.subplot(222), plt.plot(hist2, color='g'),
# plt.subplot(223), plt.plot(hist3, color='r')
# plt.xlim([0, 256])
# plt.show()

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# (thresh, binary_img) = cv.threshold(gray, 128, 255, cv.THRESH_BINARY)
# (thresh, binary_img) = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
# cv.imwrite('bus_bin.jpg', binary_img)
# cv.imshow('Binary Image', binary_img)
# cv.imshow('Color Image', imread)
# cv.imshow('Gray Image', gray)
# Order -> BGR

# # red
# image_red = img.copy()
# image_red[:, :, 1] = 0
# image_red[:, :, 0] = 0
#
# # green
# image_green = img.copy()
# image_green[:, :, 2] = 0
# image_green[:, :, 0] = 0
#
# # blue
# image_blue = img.copy()
# image_blue[:,:,2] = 0
# image_blue[:,:,1] = 0
#
# cv.imshow('Color Image', img)
# cv.imshow('Red Channel', image_red)
# cv.imshow('Green Channel', image_green)
# cv.imshow('Blue Channel', image_blue)
#
# cv.waitKey()
# cv.destroyAllWindows()
