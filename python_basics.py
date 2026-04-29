#variables
x = 1
print(x)

x = x + 2
print(x)

#lists
scores = [50, 70, 90]
print(scores[2])
list_a = [0, 1, 2, 3, 4]
print(list_a)

scores[2] = 0
print(scores)

sum(scores)

#2D lists
score_table = [['A', 'B', 'C'], [50, 70, 90]]
print(score_table[0])
print(score_table[0][2])

#for
for i in range(0, 3):
    print("Hi", i)

#NumPy
import numpy as np
array_a = np.array([5, 6, 8])

# Python list
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

# Convert list to np.ndarray
a = np.array(a)
b = np.array(b)

print("a: ", a)
print("b: ", b)

# Checking the type of a and b
print("type of a:", type(a))
print("type of b:", type(b))

# Convert np.ndarray back to list
a_list = a.tolist()
print(a_list)
print(type(a_list))

a = np.array([2, 4])
b = np.array([2, 1])
lista = a + b
print(lista)

# python lists
a = [3 , 6, 9]
b = [1, 5, 10]
print(a + b)

# NUMPY
# (1) Create two 1-dimensional np.ndarray arrays with your favorite values as elements, 
# and use the type() function to confirm that they are of type np.ndarray.

# (1)
a = np.array([3, 6, 9])
b = np.array([1, 5, 10])
print("type of a:", type(a))
print("type of b:", type(b))

# (2)
print("Addition", a + b)
print("Subtraction", a - b)
print("Multiplication", a * b)
print("Division", a / b)

print(" ")
"""
(3) Create a function that takes a 1-dimensional array as input and outputs a 1-dimensional array where the input is normalized.
Here, normalization of a vector (using the L2 norm) means scaling the original vector
so that the square root of the sum of the squares of all its elements equals 1.
In this task, please implement the function using only Numpy's universal operations and functions.
"""

def normalize_l2(arr):
    """
    Normalize a 1-dimensional array using L2 norm.
    
    Parameters:
    arr (numpy.ndarray or list): Input 1-dimensional array
    
    Returns:
    numpy.ndarray: Normalized array where sqrt(sum(x_i^2)) = 1
    """
    # Convert to numpy array if it's a list
    arr = np.array(arr)
    
    # Calculate L2 norm: sqrt(sum of squares)
    l2_norm = np.sqrt(np.sum(arr ** 2))
    
    # Avoid division by zero
    if l2_norm == 0:
        return arr
    
    # Normalize by dividing each element by the L2 norm
    normalized = arr / l2_norm
    
    return normalized

# Example usage:
if __name__ == "__main__":
    # Test with a sample array
    test_array = [3, 4]
    result = normalize_l2(test_array)
    print(f"Original: {test_array}")
    print(f"Normalized: {result}")
    print(f"L2 norm of normalized array: {np.sqrt(np.sum(result ** 2))}")
    
    # Another example
    test_array2 = [1, 2, 3, 4, 5]
    result2 = normalize_l2(test_array2)
    print(f"\nOriginal: {test_array2}")
    print(f"Normalized: {result2}")
    print(f"L2 norm of normalized array: {np.sqrt(np.sum(result2 ** 2))}")

# Practice Question
# (1) For any array you create, retrieve and display the first value 
# from the front and the first value from the back.
a = np.array([1, 3, 5, 8])
print("First value from the front:", a[0])
print("First value from the back:", a[-1])

# (2) Implement a function that takes a one-dimensional Numpy array 
# with integer values as an argument and outputs an array containing elements 
# that are either odd (leave a remainder of 1 when divided by 2) or leave a remainder of 2 when divided by 4.

def make_bool_ids(a):
    """
    Takes a 1D numpy array with integer values and returns an array
    containing only elements that are either:
    - odd (remainder 1 when divided by 2), OR
    - leave remainder 2 when divided by 4
    
    Parameters:
    a (np.ndarray): 1D array of integers
    
    Returns:
    np.ndarray: Filtered array with only elements meeting the conditions
    """
    # Condition 1: odd numbers (remainder 1 when divided by 2)
    is_odd = (a % 2 == 1)
    
    # Condition 2: remainder 2 when divided by 4
    remainder_2_mod_4 = (a % 4 == 2)
    
    # Combine conditions with OR to create boolean mask
    mask = is_odd | remainder_2_mod_4
    
    # Filter the array using the mask
    b = a[mask]
    
    return b

# Test with your example
if __name__ == "__main__":
    a = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
    result = make_bool_ids(a)
    
    print("Original array:", a)
    print("Filtered array:", result)
    
    # Verify which elements are kept
    print("\nVerification:")
    for val in a:
        is_odd = (val % 2 == 1)
        rem2_mod4 = (val % 4 == 2)
        kept = is_odd or rem2_mod4
        print(f"Value {val}: odd={is_odd}, rem2_mod4={rem2_mod4}, kept={kept}")