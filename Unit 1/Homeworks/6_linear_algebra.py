import numpy as np
import cv2
from matplotlib import pyplot as plt
from numpy.linalg import norm


# You are given a colored image, read the image and apply the following operations to it:
# Transpose.
# image = cv2.imread('splash.jpg',0)
# T = image.T.astype(np.uint8)
# plt.imshow(T,cmap='gray')
# plt.show()

# Check if the matrix is one or many of the special types we have seen (diagonal, triagonal...).

mat1 = np.matrix([[1,0,0],
                 [0,2,0],
                 [0,0,3]
                 ])
is_diag_mat = np.allclose(mat1, np.diag(np.diag(mat1)))

if is_diag_mat:
  print('Matrix is diagonal')
else:
  print('Matrix is not diagonal')


# Choose a column vector and calculate both norms that we've seen
mat = np.arange(0,25).reshape(5,5)
X = mat[:,:1]

l1 = norm(X)

print(l1)

l2 = norm(X,1)
print(l2)