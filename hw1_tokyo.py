# Implement a function that takes a 1D NumPy array of integers 
# and returns an array containing elements that are multiples of 5 
# and leave a remainder of 1 when divided by 2.

# 1. Import libraries
import numpy as np

# 2. Define a 1D NumPy array
a = np.array([3, 6, 9, 12, 15])

# 3. Define the homework function
# Fill in !!WRITE ME!! (remember that only this homework function should be submitted)
def homework(a):
    my_result = a[(a % 5 == 0) & (a % 2 == 1)]
    return my_result

result = homework(a)
print(result)

import ast
import inspect


def hw_public_tests():
    print("=== Public Tests ===")

    source = inspect.getsource(homework)
    tree = ast.parse(source)

    # Test 1: Disallow import statements
    print("Test 1: Check for import statements...", end=" ")
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            print("NG")
            print("  homework() contains import statements. Please remove them.")
            return
    print("OK")

    print("=== All Public Tests Passed ===")


hw_public_tests()
print(homework(a))