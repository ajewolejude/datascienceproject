import numpy as np
arr = np.arange(0,12)
print (arr)
print (arr[0:6])

arr[2:5] = 20
print (arr)

arr2 = arr[3:6]

arr2[:] = 29

print (arr2)
print (arr)

# creating new array copy

arrcopy = arr.copy()
