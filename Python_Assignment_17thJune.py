#!/usr/bin/env python
# coding: utf-8

# 1. What is the role of try and exception block?
# The try block contains the code that might raise exception. It allows you to specify the section of code that you want to monitor for exceptions. Except block contains the code that will be executed if exception raises.

# 2. What is the syntax for a basic try-except block?
# 
# try:
# #block of code
# #............
# 
# except:
# #executed if error in the try block
# #...............

# 3. What happens if an exception occurs inside a try block and there is no matching
# except block?
# 
# If an exception occurs inside a try block and there is no matching except block then Python will execute the built in classes appropriate for that particular exception and the execution stops.

# 4. What is the difference between using a bare except block and specifying a specific
# exception type?
# 
# The bare except block handles all exceptions but will not be able to specify the specific reason for which the exception had occurred.
# But, specific exception type will be able to handle only that particular exception. If any other exceptions occur apart from the one listed in the program, then will execute the buit in python exceptions.

# 5. Can you have nested try-except blocks in Python? If yes, then give an example.
# 
# Yes, we can have nested try-except blocks in Python.

# dict={'a':5, 'b':8, 'c':10, 'd':100}
# 
# try:
#     print("value of d: ", dict['d'])     
#         
#     try:
#         print("value of a: ", my_dict['a'])
#         
#     except NameError:
#         print("Entered invalid name")
#         
# except KeyError:
#     print("Entered Key is unavailable.") 
# 
#     

# 6. Can we use multiple exception blocks, if yes then give an example.
# Yes we can have multiple exception blocks.

# try:
#     a=int(input("Enter the first number: "))
#     b=int(input("Enter the second number: "))
#     
#     sum = a+b
#     print("sum", total)
# 
# 
# except ValueError:
#     print("Entered non integer value")
#             
# except NameError:
#     print("Entered name is unavailable")
#     

# 7. Write the reason due to which following errors are raised:
# a. EOFError :          Raised when the input() function hits an end-of-file condition (EOF).
# b. FloatingPointError :Raised when a floating point operation fails.
# c. IndexError :        Raised when a sequence subscript (index) is out of range.
# d. MemoryError :       Raised when an operation runs out of memory.
# e. OverflowError :     Raised when the result of an arithmetic operation is too large to be expressed.
# f. TabError :          Raised when the result of an arithmetic operation is too large to be expressed.
# g. ValueError :        Raised when a built-in operation or function receives an argument that has the 
#                    right type but an inappropriate value.

# 8. Write code for the following given scenario and add try-exception block to it.
# 
# a. Program to divide two numbers   

# try:
#     a=int(input("Enter the numerator: "))
#     b=int(input("Enter the denominator: "))
#     div=a/b
#     print("result", div)
#     
# except ZeroDivisionError:
#     print("Do not enter zero for the denominator")
# except ValueError:
#     print("Please enter integers")

# Enter the numerator: 3
# Enter the denominator: 3.2
# Please enter integers

# b. Program to convert a string to an integer
# 

# try:
#     s= input("Enter a string: ")
#     integer = int(s)
#     print("result_integer", integer)
#     
# except ValueError:
#     print("Please enter only digits")

# Enter a string: 20
# result_integer 20

# c. Program to access an element in a list

# try:
#     list=[i for i in input("Enter the list: ").split(',')]
#     print(l[10])
#     
# except IndexError:
#     print("Entered wrong index")

# Enter the list: 1,2,3,4,5,6,7,8,9
# Entered wrong index

# d. Program to handle a specific exception

# try:
#     l=['apples', 'oranges', 'grapes']
#     print([l[3]])
# 
# except IndexError:
#     print("Invalid index specified")
#     

# e. Program to handle any exception

# try:
#     a=10
#     b=20
#     sum = a+b+c
#     print("sum: ",sum)
#     
# except:
#     print("Please check whether all values are specified")
