import cv2 as cv

img = cv.imread("Photos/cats.jpeg")
cv.imshow("Cats", img)

# Averaging
average = cv.blur(img, (3, 3))
cv.imshow("Average Blur", average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("Gaussian Blur", gauss)

# Medium Blur
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)

bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)

