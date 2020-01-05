import numpy as np

arr = np.arange(10)
print(arr)

#to save array

#new file create saved_array.npy
np.save('saved_array', arr)

new_saved_array = np.load('saved_array.npy')
print(new_saved_array)

# Save Multiple arrays
array_1 = np.arange(10)
array_2 = np.arange(20)

np.savez('saved_archive.npz',x = array_1,y = array_2)

load_archive = np.load('saved_archive.npz')

print ('load_archive[x] is')
print (load_archive['x'])

print ('load_archive[y] is')
print (load_archive['y'])

#save to txtfile

np.savetxt('notepadfile.txt',array_1,delimiter=',')

#loading of txt files
load_txt_file = np.loadtxt('notepadfile.txt',delimiter=',')
print ("load_txt_file is")
print (load_txt_file)