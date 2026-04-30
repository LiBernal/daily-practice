#Codédex - python basics practice

""" Create a temperature.py program that converts a number from Fahrenheit (°F) to Celsius (°C).
Google the current temperature of Brooklyn, NY (where Codédex is based) in °F. """
farenheit = 52
celsius = (farenheit - 32)/1.8
print(celsius)

# The % modulo operator doesn’t give you the result of a division – it gives you the remainder.
score = 5 % 3       # score is 2
score = 5 % 2       # score is now 1
score = 5 % 1       # score is now 0
print(score)

""" 5 divided by 3 is 1, with a remainder of 2.
5 divided by 2 is 2, with a remainder of 1.
5 divided by 1 is 5, with a remainder of 0. """

# Exponents
score = 2 ** 2      # score is 4
score = 2 ** 3      # score is now 8
score = 2 ** 4      # score is now 16
print(score)        # Output: 16

"""The body mass index (BMI) was created by a Belgian mathematician in the 1850s and 
it's used by health and nutrition professionals to quickly estimate body fat.
The formula is pretty simple: Take an individual's weight (mass) in kilograms and 
dividing it by their height in meters, squared. """
mass = 56
height = 1.70
bmi = mass / (height ** 2)
print(bmi)

# Pythagorean theorem
import math

print("Welcome, Let's Calculate the Pythagorean theorem!")
a = int(input("Lenght of the short side: "))
b = int(input("Lenght of the other short side: "))
hypo = math.sqrt((a**2) + (b**2))
print(hypo)
# or
hypo = ((a**2) + (b**2))**0.5
print(hypo)

# Quadratic formula
import math
a = 2
b = -5
c = -3
chicharronera_raiz1 = (-b + math.sqrt((b**2 - 4*a*c))) / (2*a)
chicharronera_raiz2 = (-b - math.sqrt((b**2 - 4*a*c))) / (2*a)
print(chicharronera_raiz1)
print(chicharronera_raiz2)