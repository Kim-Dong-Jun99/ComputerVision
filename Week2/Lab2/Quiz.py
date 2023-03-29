import cv2 as cv
import sys

quiz1 = cv.imread('../Lab2 Image/noise_quiz1.png')
quiz2 = cv.imread('../Lab2 Image/noise_quiz2.png')
quiz3 = cv.imread('../Lab2 Image/noise_quiz3.png')

if quiz1 is None:
    sys.exit("파일을 찾을 수 없습니다")


"""
Median Blur
"""
quiz1_medianBLur7 = cv.medianBlur(quiz1, 7) # ksize = 7
quiz2_medianBLur7 = cv.medianBlur(quiz2, 7) # ksize = 7
quiz3_medianBLur7 = cv.medianBlur(quiz3, 7) # kisze = 7

"""
Gaussian Filtering
"""
quiz1_dst = cv.GaussianBlur(quiz1, (0, 0), 5)  # output image (Sigma = 5) size is dependent on sigma
quiz2_dst = cv.GaussianBlur(quiz2, (0, 0), 5)  # output image (Sigma = 5) size is dependent on sigma
quiz3_dst = cv.GaussianBlur(quiz3, (0, 0), 5)  # output image (Sigma = 5) size is dependent on sigma

cv.imshow("Image 1 with MedianBlur 7", quiz1_medianBLur7)
cv.imshow("Image 2 with MedianBlur 7", quiz2_medianBLur7)
cv.imshow("Image 3 with MedianBlur 7", quiz3_medianBLur7)

cv.imshow("Image 1 with GaussianFilter sigma = 5", quiz1_dst)
cv.imshow("Image 2 with GaussianFilter sigma = 5", quiz2_dst)
cv.imshow("Image 3 with GaussianFilter sigma = 5", quiz3_dst)
cv.waitKey()
cv.destroyAllWindows()
