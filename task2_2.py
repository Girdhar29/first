#     2. Using NumPy, generate a 5x5 matrix with random integers. Perform:
#         - Matrix addition and multiplication.
#         - Calculate row and column means.


#import numpy
import numpy as np


# Random generate 5x5 matrices with random integers  from 1 to 10

#1st metrix
M1 = np.random.randint(1, 10, size=(5, 5))
print("Matrix 1:\n", M1)

#2nd metrix
M2 = np.random.randint(1, 10, size=(5, 5))
print("\nMatrix 2:\n", M2)


# Addition of two random metrix
MetrixSum = M1 + M2
print("\nMatrix Sum:\n", MetrixSum)


# Matrix multiplication
MatrixMulti = np.dot(M1, M2)
print("\nMatrix Product:\n", MatrixMulti)


# Calculate row means
RowMeans1 = np.mean(M1, axis=1)
print("\nRow Means of Matrix 1:\n", RowMeans1)

RowMeans2 = np.mean(M2, axis=1)
print("\nRow Means of Matrix 2:\n", RowMeans2)
# Calculate column means
ColMeans1 = np.mean(M1, axis=0)
print("\nColumn Means of Matrix 1:\n", ColMeans1)

ColMeans2 = np.mean(M2, axis=0)
print("\nColumn Means of Matrix 2:\n", ColMeans2)








