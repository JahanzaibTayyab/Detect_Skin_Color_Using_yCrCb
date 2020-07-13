import cv2
import numpy as np
import matplotlib.pyplot as plt

# Defining YCrCb Threadholds
min_YCrCb = np.array([0, 133, 77], np.uint8)
max_YCrCb = np.array([235, 173, 127], np.uint8)
# Read the picture
image = cv2.imread("kid2.jpg")
# Converting into the BRG to YCrCb
imageYCrCb = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
# dectect the skin color region
skinRegionYCrCb = cv2.inRange(imageYCrCb, min_YCrCb, max_YCrCb)
# Change the detect skin color into bit array
skinYCrCb = cv2.bitwise_and(image, image, mask=skinRegionYCrCb)
# save the array
cv2.imwrite("kid2.jpg", np.hstack([image, skinYCrCb]))
