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
Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
Salary(Lakhs) : Tax(%)

Below 5 : 0%
5-10 : 10%
10-20 : 20%
aboove 20 : 30%
'''
"""
ctc = float(input("Enter CTC in lakhs: "))

hra = ctc * 10 / 100
da = ctc * 5 / 100
pf = ctc * 3 / 100

if ctc < 5:
    tax = 0
elif ctc <= 10:
    tax = ctc * 10 / 100
elif ctc <= 20:
    tax = ctc * 20 / 100
else:
    tax = ctc * 30 / 100

annual_salary = ctc - hra - da - pf - tax

monthly_salary = annual_salary / 12

print("Monthly Salary =", monthly_salary, "Lakhs")
"""
'''
Problem 2: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
'''
"""
a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if a + b + c == 180:
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")
"""
'''
Problem 3: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.
'''
"""
cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

if sp > cp:
    print("Profit")
elif cp > sp:
    print("Loss")
else:
    print("No Profit No Loss")
"""
'''
Problem 4: Write a menu-driven program -
          cm to ft
          km to miles
          USD to INR
          exit
'''
"""
choice = 0

while choice != 4:
    print("\nMenu")
    print("1. CM To Ft")
    print("2. KM To miles")
    print("3. USD To INR")
    print("4. Exit")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        cm = float(input("Enter length in cm:"))
        ft = cm / 30.48
        print("Length in feet  =", ft)

    elif choice == 2:
        KM = float(input("Enter length in KM"))
        miles = KM * 0.621371
        print("Length in miles =", miles)

    elif choice == 3:
        USD = float(input("Enter amount in USD:"))
        INR = USD * 94
        print("Amount in INR =", INR)

    elif choice == 4:
        print("Program Exited")

    else:
        print("Ivalid choice:")
"""
'''
Problem 5 - Exercise 12: Display Fibonacci series up to 10 terms.
            Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it.
            The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21.
             The next number in this series above is 13+21 = 34
'''
# Initialize the first two terms of the Fibonacci sequence
term1 = 0
term2 = 1

# Print the first term
print(term1, end=' ')

# Print the second term
print(term2, end=' ')

# Loop to calculate and print the remaining terms
for i in range(2, 10):
    # Calculate the next term in the sequence
    next_term = term1 + term2

    # Print the next term
    print(next_term, end=' ')

    # Update the values of term1 and term2 for the next iteration
    term1 = term2
    term2 = next_term









