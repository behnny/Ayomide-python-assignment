# import NumPy
import numpy as np

# Create a 5*5 array with random integer from 1 to 100
array = np.random.randint(1, 101, (5, 5))

# Display the array
print("5 * 5 Random Array")
print(array)

# Question 2

import numpy as np

# Create a 5*5 array with random integers from 1 to 100
array = np.random.randint(1, 101, (5, 5))

print("5 * 5 Random Array")
print(array)

# Indexing
print("First element:", array[0, 0])

# Slicing
print("First two rows:")
print(array[:2])

# Boolean Indexing
print("Values greater than 50:")
print(array[array > 50])

# Transpose
print("Transpose of the array:")
print(array.T)

 # Universal Functions

# Question 3

import numpy as np

# Create a 5*5 array with random integers from 1 to 100
array = np.random.randint(1, 101, (5, 5))

print("5 * 5 Random Array")
print(array)

# Indexing
print("First element:", array[0, 0])

# Slicing
print("First two rows:")
print(array[:2])

# Boolean Indexing
print("Values greater than 50:")
print(array[array > 50])

# Transpose
print("Transpose of the array:")
print(array.T)

 # Universal Functions
print("Square Root:")
print(np.sqrt(array))

print("Mean:", np.mean(array))

print("Standard Deviation:", np.std(array))
