# Blurring Techniques

import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging
# If you have an image with 3x3 dimensions then the blurring will be done for the middle pixel
# More blur as compared to gaussian
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
# If you have an image with 3x3 dimensions then the blurring will be done for each pixel
# Less blur as compared to averaging
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
# Concentrated to median
# More effective in reducing noise as compared to averaging
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
# You blur the image but it do not lose edges
# The most effective way of blurring images
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)