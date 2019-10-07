import numpy as np

a = np.array([1, 2, 3], dtype='int16')
b = np.array([2, 3, 4], dtype='int64')
print(a, a.itemsize, a.size, a.dtype)
print(b, b.itemsize, b.size, b.dtype)
c = a*b
print(c, c.itemsize, c.size, c.dtype, c.shape)
print('--'*20)
"""----------------- 2d Array---------------------"""

a1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8], [2, 3, 4, 5, 6, 7, 8, 9]])
b1 = np.array([[2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8, 9, 10]])

print("2D Array: \n", a1)
print("Dimensions: ", a1.ndim)
print("Shape[a1]: ", a1.shape)
print("Shape[b1]: ", b1.shape)
print("Row: ", a1.shape[0])
print("All elements of row 1: ", a1[0, :])
print("ALl elements of columns 1", a1[:, 0])
print('--'*20)
"""-------------------------------------------------"""
c1 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(c1)
print(c1[0, 1, 0])  # fetch c1[0] {[1, 2],[3, 4]} ->c1[0][1] {[3, 4]} ->c1[0, 1, 0] {3}
print(c1[:, 1])  # for all the rows , fetch its 1st column
print('--'*20)

"""---------Initialising different types of arrays--------------------"""
a3 = np.zeros((2, 3))  # all zeros matrix.
print("0s matrix: ", a3)
a4 = np.ones((2, 3, 4))  # all ones matrix.
print("1s matrix: ", a4)
a5 = np.full((3, 3), 99)
print("Any other number: ", a5)
a6 = np.full_like(a, 5)  # find the a [1,2,3] structure and tweak it with elements.
print("Cloning other array structures: ", a6)
a7 = np.random.rand(4, 2)
print("Creating random array: ", a7)
a8 = np.random.random_sample(a.shape)
print("Cloning random array structures from a: ", a8)
a9 = np.random.randint(8, 11, size=(4, 3))  # 8 is start value, 11 is end value (excluded)
print(a9)
a10 = np.identity(5)
print("The identity matrix: ", a10)
arr = np.array([[1, 2, 3]])
a11 = np.repeat(arr, 3, axis=1)  # repeat contents in x direction
print("Axis=1: ", a11)
a11 = np.repeat(arr, 3, axis=0)  # repeat contents in y direction.
print("Axis=0:\n", a11)
print('--'*20)
"""------------------------------Exercise--------------------------"""
""" print the following matrix:
1 1 1 1 1
1 0 0 0 1
1 0 9 0 1
1 0 0 0 1
1 1 1 1 1
"""
solution1 = np.ones((5, 5))
print(solution1)
zeroes1 = np.zeros((3, 3))
print(zeroes1)
solution1[1:4, 1:4] = zeroes1
solution1[2, 2] = 9
print(solution1)
print('--'*20)

"""----------------copying arrays--------------------------------"""
""" be careful while copying without copy function. it will also
    replace the original value of the array which is copied.

"""
a = np.array([1, 2, 3])
b = a
b[0] = 100
print("Without copy():\n", b, a)
# the value of a will also change, so prevent it using copy() method.
b = a.copy()
b[0] = 200
print("With copy(): \n", b, a)
