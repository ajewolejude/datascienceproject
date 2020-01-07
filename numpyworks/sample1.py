import numpy as np

list1 = [2,4,6,8]
list2 = [1,3,5,7]

#printing one list in array
array1 = np.array(list1)
print(array1)

#printing two list in array
array2 = np.array([list1, list2])
print(array2)

#print arrray dimension
print (array2.shape)

#print datattype
print (array2.dtype)

new_array1 = np.zeros(3) #creates a new numpy array  with (1*3) of zeros.
new_array2 = np.ones([5,3]) #all elements as 1
new_array3 = np.eye(5)
new_array4 = np.arange(6,20,5)
print (new_array1)
print (new_array2)
print (new_array3)
print (new_array4)

