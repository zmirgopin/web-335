#code attribution
#author: Zahava Gopin
#title: gopin_calculator.py
#description: python calculator
#date: 29 March 2023

#function to add two variables
def add(a,b):
    #results of the function
    total =  a+b
    #formatted string to display results
    addition = f"{a} + {b} is {total}"
    #display results
    print(addition)

#function to subtract two variables
def subtract(a,b):
    total = a-b
    subtraction = f"{a} - {b} is {total}"
    print(subtraction)

#function to divide two variables
def divide(a,b):
    total = a/b
    division =  f"{a} / {b} is {total}"
    print(division)

#function to multiply two variables
def multiply(a,b):
    total = a*b
    multiplication = f"{a} * {b} is {total}"
    print(multiplication)

#passing values into each function
add(10, 2)
subtract(10, 2)
divide(10, 2)
multiply(10, 2)


