import numpy as np
a = np.array([1, 2, 3, 4])
a += 2
print("Adding 2 to each element:", a)
a *= 2
print("Multiply 2 to each element: ", a)
b = np.array([1, 0, 1, 0])
print("Adding two arrays:", b+a)
""""----------------Trigonometric Analysis----------------"""
print("Cosine values are: ", np.sin(a))


""" for more: Check https://scipy.org/doc/numpy/refrences/routines.math.html """


"""-----------------Linear Algebra------------------------"""
a = np.ones((2, 3))
b = np.full((3, 3), 2)
print("Matrix Multiplication: ", np.matmul(a, b))
c = np.random.randint(4, 10, size=(3, 3))
print(c)
print("Determinant of Matrix: ", np.linalg.det(c))

"""
Some other operations:
1. Trace
2. Singular vector decomposition
3. Eigenvalues
4. Matrix Norms
5. Inverse
etc...(Refer to the link in markdown file)

"""

"""---------------------STATISTICS---------------------------"""

stats = np.array([[1, 2, 3], [4, 5, 6]])
print(stats)
print("Min element:", np.min(stats), ", Max element: ", np.max(stats))
print("Min element:", np.min(stats, axis=1), ", Max element: ", np.max(stats, axis=1))
print("Sum of elements:", np.sum(stats))
print("Sum of elements [per row]:", np.sum(stats, axis=1))
print("Sum of elements [per columns]:", np.sum(stats, axis=0))

