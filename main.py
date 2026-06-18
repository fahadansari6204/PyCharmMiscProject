                                             # CampusX
# Session 1 - Python Fundamentals

# topic-
"""
Output
Data Types
Variables
Comments
Keywords & Identifiers
User Input
Type Conversion
Literals
"""

# TASK 1
'''
Q1 :- Print the given strings as per stated format.

Given strings:-
"Data" "Science" "Mentorship" "Program" 
"By" "CampusX"

Output:-
Data-Science-Mentorship-Program-started-By-CampusX
'''

"""
print("Data-Science-Mentorship-Program-Started-By-CampusX")
"""
'''
Q2:- Write a program that will convert celsius value to fahrenheit.
'''
"""
Celsius = float(input("Enter temperature in Celsius:"))
Fahrenheit = (Celsius * 9/5) + 32
print(f'{Celsius}°C is Equal to {Fahrenheit}°F')       #yaha f' ' ko f-string kehte hain. or F-string me { } ke andar variable ki value print hoti hai.
"""
'''
Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.
'''
"""
a = int(input("Enter your a no: "))
b = int(input("Enter your b no: "))

temp = a                 #swap karne ke liye temp bana pada or isme a ka value dalna pada
a = b                    #yaha a ka value khali hogya isme b ka value aa gya 
b = temp                 #or ab yaha b me koi value nahi tha to yaha temp ke = hone se temp ka value a gya.
print("After swapping:")
print("a =", a)          #comma (,) ka use tab karte hai jab ak se jad chiz print karna ho ,jaise yaha Print ("a ="), Print (a) ki value.
print("b =", b)          #same isme bhi ("b =", b).
"""

'''
Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.
'''
"""
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5   #Ye formula Pythagoras Theorem par based hai. iska use hua hai distance nikalne ke liye

print("Euclidean Distance =", distance)
"""

'''
Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.
'''
"""
p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

si = (p * r * t) / 100           #Simple Interest nikalne ka formula hai.

print("Simple Interest =", si)
"""
'''
Q6:- Write a program that will tell the number of dogs and chicken are there
     when the user will provide the value of total heads and legs.
'''
"""
heads = int(input("Enter number of heads: "))
legs = int(input("Enter number of legs:"))

dogs = (legs - 2 * heads) // 2
chicken = heads - dogs

print("Dogs =", dogs)
print("Chicken =", chicken)
"""
'''
Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.
'''
"""
n = int(input("Enter n: "))

sum_of_squares = n * (n + 1) * (2 * n + 1) / 6  #formula of square

print(sum_of_squares)
"""
'''
Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.
'''
"""
a = int(input("Enter first term: "))
b = int(input("Enter second term: "))
n = int(input("Enter N: "))

d = b - a

nth_term = a + (n - 1) * d #formula of nth term

print("Nth term is:", nth_term)
"""
'''
Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.
'''
"""
num1 = int(input("Enter numerator of first fraction: "))
den1 = int(input("Enter denominator of first fraction: "))

num2 = int(input("Enter numerator of second fraction: "))
den2 = int(input("Enter denominator of second fraction: "))

sum_num = (num1 * den2) + (den1 * num2)     #formula of sum of numerator
sum_den = den1 * den2                       #formula of sum of denominator

print("Sum =", sum_num, "/", sum_den)
"""
'''
Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained?
                                                                         Assume all the inputs are provided by the user.

Input:
Dimensions of the milk tank
H = 20cm, L = 20cm, B = 20cm

Dimensions of the glass
h = 3cm, r = 1cm
'''
"""
# Input tank dimensions
H = float(20)
L = float(20)
B = float(20)

# Input glass dimensions
h = float(3)
r = float(1)

# Volume of tank
tank_volume = H * L * B

# Volume of glass
glass_volume = 3.14 * r * r * h

# Number of glasses
glasses = int(tank_volume / glass_volume)

print("Number of glasses =", glasses)
"""

#Session 2 - Operators + If-Else + Loops
# topic-
"""
Operators in Python
If-else in Python
Modules in Python:-    math/keywords/random/datetime
Loops in Python
"""

# TASK 2
'''

'''
import datetime

print(datetime.datetime.now())
a = 2
b = 4

c = (a + b)
print(c)

