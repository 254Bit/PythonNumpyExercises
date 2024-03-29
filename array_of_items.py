#Following is the provided numPy array. 
# sampleArray = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
# Return array of items by taking the second column from all rows

import numpy as np

sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])

# Print (sampleArray)
new_array = sampleArray[...,1]
print(new_array)