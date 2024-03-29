# Create a 5X2 integer array from a range between 300 to 400 
# such that the difference between each element is 10

import numpy as np

my_array = np.arange(300,400,10)
my_array = my_array.reshape(5,2)
print(my_array)
