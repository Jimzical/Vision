import cv2
import numpy as np

file = "CheckBoard/dis1.jpg"
image = cv2.imread(file)

cv2.imshow('img', image)
cv2.waitKey(0)
