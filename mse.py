import cv2
import numpy as np
import time
# Read images
image1 = cv2.imread("dhoni_img1.png")
cv2.imshow("originalImage",image1)
image2 = cv2.imread("dhoni_img2.png")
cv2.imshow("defectImage",image2)

def mse(image1, image2):  # Mean Square Error Algorithm
     h, w = image1.shape
     diff = cv2.subtract(image1, image2)
     err = np.sum(diff**2)
     mse = err/(float(h*w))
     return mse, err
print("Image matching Error between the two images:", int(mse))
cv2.waitKey(0)
cv2.destroyAllWindows()