import numpy as np
import matplotlib.pyplot as plt

axis_values = np.arange(-100,100,10)

xaxis, yaxis = np.meshgrid(axis_values,axis_values)

#print ("dx:")
#print (dx)

#print ("dy")
#print (dy)

function1 = 2*xaxis+3*yaxis
function2 = np.cos(xaxis)+np.cos(yaxis)

print (function1)
print (function2)

#replace function2 by function1 to get graph of function1.
#plotting the function on graph
plt.imshow(function2)
plt.title("function cos plot")
plt.colorbar()
plt.savefig('myplot.png')

