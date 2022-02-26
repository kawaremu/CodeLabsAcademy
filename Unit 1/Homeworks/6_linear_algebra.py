import numpy as np
import cv2
from matplotlib import pyplot as plt



image = cv2.imread('splash.jpg')

transpose = image.T.astype(np.uint8)
plt.imshow(transpose)
plt.show()


test_matrix = np.array([7,4,1,2,5,4,8,7,4,5,2,1,4,5])

