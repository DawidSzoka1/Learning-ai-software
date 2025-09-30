import numpy as np

a = np.ones((2, 3))
b = np.full((3, 2), 2)

print(a,'\n', b)

print(np.matmul(a, b))

print(np.linalg.det(np.matmul(a, b)))