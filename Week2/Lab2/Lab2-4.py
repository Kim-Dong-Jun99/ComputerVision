import cv2 as cv
import numpy as np

"""
Image Pyramid
"""

src = cv.imread('../Lab2 Image/pizza_512.jpg', cv.IMREAD_COLOR)
height, width, channel = src.shape

dst = cv.pyrDown(src)
dst2 = cv.pyrUp(src, dstsize=(width * 2, height * 2), borderType=cv.BORDER_DEFAULT)
# dst2 = cv.pyrUp(src)

cv.imshow("src", src)
cv.imshow("pyrDown", dst)
cv.imshow("pyrUp", dst2)
print(dst2.shape)

"""
Image Blending
"""
pizza = cv.imread('../Lab2 Image/pizza_512.jpg')
burger = cv.imread('../Lab2 Image/burger_512.jpg')

print(pizza.shape)
print(burger.shape)

pizza_burger = np.hstack((pizza[:, :256], burger[:, 256:]))

# generate Gaussian pyramid for pizza
pizza_copy = pizza.copy()
gp_pizza = [pizza_copy]
for i in range(6):
    pizza_copy = cv.pyrDown(pizza_copy)
    gp_pizza.append(pizza_copy)

# generate Gaussian pyramid for burger
burger_copy = burger.copy()
gp_burger = [burger_copy]
for i in range(6):
    burger_copy = cv.pyrDown(burger_copy)
    gp_burger.append(burger_copy)

# generate laplacian pyramid for pizza
pizza_copy = gp_pizza[5]
lp_pizza = [pizza_copy]
for i in range(5, 0, -1):
    gaussian_expanded = cv.pyrUp(gp_pizza[i])
    laplacian = cv.subtract(gp_pizza[i - 1], gaussian_expanded)
    lp_pizza.append(laplacian)

# generate laplacian pyramid for burger
burger_copy = gp_burger[5]
lp_burger = [burger_copy]
for i in range(5, 0, -1):
    gaussian_expanded = cv.pyrUp(gp_burger[i])
    laplacian = cv.subtract(gp_burger[i - 1], gaussian_expanded)
    lp_burger.append(laplacian)

# Now add left and right halves of images in each level
pizza_burger_pyramid = []
n = 0
for pizza_lap, burger_lap in zip(lp_pizza, lp_burger):
    n += 1
    cols, rows, ch = pizza_lap.shape
    laplacian = np.hstack((pizza_lap[:, 0:int(cols / 2)], burger_lap[:, int(cols / 2):],))
    pizza_burger_pyramid.append(laplacian)

# now reconstruct
pizza_burger_reconstruct = pizza_burger_pyramid[0]
for i in range(1, 6):
    pizza_burger_reconstruct = cv.pyrUp(pizza_burger_reconstruct)
    pizza_burger_reconstruct = cv.add(pizza_burger_pyramid[i], pizza_burger_reconstruct)

cv.imshow("pizza", pizza)
cv.imshow("burger", burger)
cv.imshow("pizza_burger", pizza_burger)
cv.imshow("pizza_burger_reconstruct", pizza_burger_reconstruct)

cv.waitKey()
cv.destroyAllWindows()
