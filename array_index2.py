import numpy as np

arr2d = np.array([[9,8,7],[6,5,4],[3,2,1]])
print (arr2d)
print (arr2d[1][2])

#slices of 2d array

slice1 = arr2d[0:3,0:3]
print (slice1)


arr2d[:2,1:] = 5
print (arr2d)

#using loops to index
arr_len = arr2d.shape[0]

for i in range(arr_len):
    arr2d[i] = i;
print (arr2d)

#one more way of accessing the rows
print (arr2d[[2,1]])

print (arr2d[[1,1]])