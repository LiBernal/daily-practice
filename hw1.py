# Función que tome un array 1D NumPy de números enteros y devuelva un array 
# que contiene elementos que son múltiplos de 5 y deja un residuo de 1 cuando se divide por 2.

# 1. Import libraries
import numpy as np

# 2. Define a 1D NumPy array
a = np.array([1, 5, 10, 3, 4, 25, 30])

# 3. Funcion
def homework(a):
  # Condicion 1: Múltiplo de 5
  cond_1 = a % 5 == 0
  # Condición 2: Residuo de 1 al dividir entre 2 (impar)
  cond_2 = a % 2 == 1
  my_result = a[cond_1 & cond_2]

  return my_result

# Test
your_answer = homework(a)
print("Your answer:", your_answer)
