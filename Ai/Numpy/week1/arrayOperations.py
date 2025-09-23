import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(np.append(arr, 2))  # append creates new array, doesnt change original array
print(arr)

print(np.delete(arr, 2))  # same with delete, delete object on index
print(arr)

arr_2 = np.array([[1, 2, 3], [1, 4, 3]])
print(arr_2)
print(np.delete(arr_2, 0)) # if axis is None array will be flattened
print(np.delete(arr_2, [0, 2], axis=1)) # axis = 0 delete in first dimension, axis = 1 in second, obj can by a list

print(arr + arr_2.flat)
print(arr - arr_2.flat)
print(arr * arr_2.flat)
print(arr / arr_2.flat)
print(np.multiply(arr, arr_2.reshape(6,)))
x1 = np.arange(8).reshape((2, 4))
x2 = np.arange(4)
print(np.multiply(x1, x2))