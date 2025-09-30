import numpy as np

a = np.random.rand(3, 3) * 100
print(a > 50)
print(a[a > 50])
print(a[a <= 50])
print(np.array([1, 2, 3, 4, 5, 6, 7, 8])[[1, 2, 7]])
b = np.array([3, 4, 5, 6, 7, 8])
print(b)
print(np.all(b > 2))

print(~((a > 50) & (a < 100)))
c = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
print(c)
print(c[[0,1], [0,2]])
print(
    c[[0, -2, -1], 3:]
)