import numpy as np

before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(before)
"""--------------------Reshaping arrays------------------"""
after = before.reshape((4, 2))
print("reshaping arrays in 4,2:", after)
after = before.reshape(2, 2 ,2)
print("reshaping arrays in 2 2 2:", after)
print("--"*20)
'''---------------------Stack Operations------------------'''
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

verticalStack = np.vstack([a, b])
print("Stack Vertically:", verticalStack)
horizontalStack = np.hstack([a, b])
print("Stack Horizontally:", horizontalStack)
c = np.ones((2, 4))
d = np.zeros((2, 2))
print("Horizontal stack:", np.hstack([c, d]))
'''--------------------------------------------------------'''
 
