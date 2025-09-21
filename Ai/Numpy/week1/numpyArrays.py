import numpy as np

one_di = np.array([1, 2, 3, 4, 5])

print(one_di)
print(type(one_di))

arr = np.array(42)

two_di = np.array(((1, 2, 3 ), (4, 5, 6)))
two_di_2 = np.array([[1,2,3], [4, 5, 6]])

print(two_di_2)
print(two_di)
print(arr.ndim)
print(one_di.ndim)
print(two_di.ndim)

five_di = np.array([1, 2, 3, 4], ndmin=5)
print(five_di)
print(five_di.ndim)

python_list = [1, 2, 3, 4, 5]
np_array = np.array(python_list)
print(np_array)
print(type(np_array))

def array_modifier(lst, value, index):
    arr = np.array(lst)
    arr = arr[:index]
    arr = np.append(arr, value)
    arr = np.append(arr, lst[index:])
    return arr

def array_modifier_insert(lst, value, index):
    arr = np.array(lst)
    arr = np.insert(arr, [index], [value, value + 5])
    return arr

print(array_modifier(python_list, 10, 2))
print(array_modifier_insert(python_list, 10, 2))