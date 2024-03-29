# Exercise 2: Create a 4X2 integer array and Prints its attributes
# Note: The element must be a type of unsigned int16. And print the following Attributes: –
# The shape of an array.
# Array dimensions.
# The Length of each element of the array in bytes.

import numpy as np


firstArray = np.empty([4,2], dtype = np.uint16)

print('The shape of the array is: ', firstArray.shape)
print('The arrays dimension is:', firstArray.ndim)
print('The item size of each element in the array is:', firstArray.itemsize)
