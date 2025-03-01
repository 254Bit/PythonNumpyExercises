# Delete the second column from a given array and insert the following new column in its place.

# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
# newColumn = numpy.array([[10,10,10]])

import numpy

print ('Printing the original array')
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
print(sampleArray)

print('Array after deleting column 2 on axis 1')
sampleArray = numpy.delete(sampleArray, 1, axis = 1)
print(sampleArray)

arr = numpy.array([[10,10,10]])

print('Array after inserting column 2 on axis 1')
sampleArray = numpy.insert(sampleArray, 1, arr, axis = 1)
print(sampleArray)
