#!/usr/bin/env python
# coding: utf-8

# 1. In Python, what is the difference between a built-in function and a user-defined function? Provide an
# example of each.

# Built in functions are pre-defined functions that come bundled with Python and can be used directly in a Python program without importing external libraries.Eg: len(), str(), input(), int(), float(), type().
# 
# A user-defined function in Python is a code block that performs a specific task and is defined by the programmer.
# 
# Eg:

# def multiplication(a,b):
#     mul=a*b
#     return mul
# 
# mul_result=multiplication(5,2)
# print("Multiplication_result: ",mul_result)
# 

# 2. How can you pass arguments to a function in Python? Explain the difference between positional
# arguments and keyword arguments.
# 
# Functions can take arguments, which are values you supply to the function so it can perform a computation with them. These arguments are placed inside parentheses after the function name.
# 
# Positional arguments are arguments that need to be included in the proper position or order.
# Eg. complex(2,8)
# 
# A keyword argument is an argument passed to a function or method which is preceded by a keyword and an equals sign.
# In general form : function(keyword=value)
# 
# Eg:complex(real=2, imag=8)

# 3. What is the purpose of the return statement in a function? Can a function have multiple return
# statements? Explain with an example.
# 
# Functions can optionally return a value using the return statement. The value that's returned can be used in other parts of your program. If no return statement is specified, the function will return None.
# 
# A function can have multiple return statements.
# Eg:

# def Calculator():
#     number_1 = float(input("Enter the first number: "))
#     number_2 = float(input("Enter the second number: "))
# 
#     # Addition
#     add_result = number_1 + number_2
# 
#     # Subtraction
#     diff_result = number_1 - number_2
# 
#     # Multiplication
#     mult_result = number_1 * number_2
# 
#     # Division
#     div_result = number_1 / number_2
#     
#     return [add_result, diff_result, mult_result, div_result]
# 
# 
# results = Calculator()
# 
# print("The sum is:", results[0])
# print("The difference is:", results[1])
# print("The product is:", results[2])
# print("The quotient is:", results[3])

# 4. What are lambda functions in Python? How are they different from regular functions? Provide an
# example where a lambda function can be useful.
# 
# Lambda functions are small, anonymous functions defined with the lambda keyword. They can take any number of arguments but can only have one expression. The arguments are not surrounded by parantheses as in regular function.
# 
# The Lambda function evaluates and returns only one value unlike in regular function.
# 
# Unlike in regular functions, Lambda functions do not require a return statement, the expression is implicitly returned.
# 
# Lamda functions can be used to evaluate single expressions and also in in filter(), map(), generator(), sorted().
# Eg:
# l=[1,2,3,4,5,6,7,8,9,10]
# list(filter(lambda x: x % 2 == 0 , l))

# 5. How does the concept of "scope" apply to functions in Python? Explain the difference between local
# scope and global scope.
# 
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
# 
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.
# 
# Eg:

# x=1000
# def scope():
#     x=10
#     print("local_scope; inside function: ", x)
#     
# scope()
# print("Global_scope; outside function: ",x)

# local_scope; inside function:  10
# Global_scope; outside function:  1000

# 6. How can you use the "return" statement in a Python function to return multiple values?
# 
# If 'return' statement returns mutiple vlaues, it can be used as a list or dictionary.
# Eg:
# return[add,multiply] 
# The values can be acessed from the list .
# 
# or 
# 
# return{'addition':add, 'multiplication':multiply}
# The values can be accessed from the dictionary by providing key after calling the function.
# 

# 7. What is the difference between the "pass by value" and "pass by reference" concepts when it
# comes to function arguments in Python?
# 
# In pass by value (also known as call by value), the argument passed to the function is the copy of of its original object. If we change or update the value of object inside the function, then original object will not change.
# In pass by reference (also known as call by reference), the argument passed to the function’s parameter is the original object. If we change the value of object inside the function, the original object will also change.

# 8. Create a function that can intake integer or decimal value and do following operations:
# a. Logarithmic function (log x)
# b. Exponential function (exp(x))
# c. Power function with base 2 (2^x)
# d. Square root

# import math
# x=float(input("Enter number: "))
# def multi_operations():       
#     y=math.log(x)
#     e=math.exp(x)
#     p=2**x
#     r=x**(1/2)
#     return [y,e,p,r]
# 
# results=multi_operations()
# print("logarithm",results[0])
# print("exponential",results[1])
# print("power",results[2])
# print("squareroot",results[3])

# Enter number: 3.6
# logarithm 1.2809338454620642
# exponential 36.59823444367799
# power 12.125732532083186
# squareroot 1.8973665961010275

# 9. Create a function that takes a full name as an argument and returns first name and last name.

# def firstname_lastname():
#     name=input("Enter Full name: ")
#     split_name=name.split()
#     return split_name
# 
# result_name=firstname_lastname()
# print("First_name ", result_name[0])
# print("Last_name ", result_name[1])

# Enter Full name: Sreepriya Kurup
# First_name  Sreepriya
# Last_name  Kurup
