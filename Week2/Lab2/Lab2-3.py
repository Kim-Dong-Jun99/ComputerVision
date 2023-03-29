import cv2 as cv
import sys
import numpy as np
myimage = cv.imread("../Lab2 Image/myimage.png")
# img = cv.imread("../Lab2 Image/lena_gray.png")
img = cv.cvtColor(myimage, cv.COLOR_BGR2GRAY)
"""
Sobel
"""

sobelx = cv.Sobel(img, -1, 1, 0, 3)
sobely = cv.Sobel(img, -1, 0, 1, 3)

abs_grad_x = cv.convertScaleAbs(sobelx)
abs_grad_y = cv.convertScaleAbs(sobely)

sobel = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

cv.imshow("Original", img)
cv.imshow("Sobel", sobel)

"""
Canny
"""

canny_img = cv.Canny(img, 100, 200)
cv.imshow("Canny", canny_img)

"""
Laplacian
"""

laplacian = cv.Laplacian(img, cv.CV_8U, ksize=3)
mask1 = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
mask2 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
mask3 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

laplacian1 = cv.filter2D(img, -1, mask1)
laplacian2 = cv.filter2D(img, -1, mask2)
laplacian3 = cv.filter2D(img, -1, mask3)
laplacian4 = cv.Laplacian(img, -1)

cv.imshow("Laplacian1", laplacian1)
cv.imshow("Laplacian2", laplacian2)
cv.imshow("Laplacian3", laplacian3)
cv.imshow("Laplacian4", laplacian4)

cv.waitKey()
cv.destroyAllWindows()
