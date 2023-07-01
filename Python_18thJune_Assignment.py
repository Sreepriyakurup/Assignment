#!/usr/bin/env python
# coding: utf-8

# 1. What is the role of the 'else' block in a try-except statement? Provide an example
# scenario where it would be useful.
# 
# The "else" keyword is used to specify a block of code that will be performed if no errors are raised.

# try:
#     a=10
#     b=20
#     sum = a+b    
# except:
#     print("The entered numbers shouls be integers")
# else:
#     print ("sum is ", sum)

# 2. Can a try-except block be nested inside another try-except block? Explain with an
# example.
# Yes we can create a nested try-except block.

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
# except KeyError: print("Entered Key is unavailable.")

# 3. How can you create a custom exception class in Python? Provide an example that
# demonstrates its usage.

# class NegativeNumber(Exception):
#     pass
# 
# def div():
#     try:
#         a = int(input("Enter first number: "))
#         b = int(input("Enter first number: "))
#         if a<0 or b<0:
#             raise NegativeNumber("Negative number not allowed")                                 
#                                                                                        
#     
#         div_result=a/b
#         return div_result
#                 
#     except ZeroDivisionError:
#                 print("Please enter non zero number as denominator")
#     except NegativeNumber as e:
#                 print(e)
#                 
# result = div()
# print("Division", result)
#     

# 4. What are some common exceptions that are built-in to Python?
# 
# ZeroDivisionError: Raised when the second argument of a division or modulo operation is zero.
# 
# TypeError: Raised when an operation or function is applied to an object of inappropriate type.
# 
# ValueError: Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.
# 
# IndexError: Raised when a sequence subscript is out of range.
# 
# KeyError: Raised when a dictionary key is not found.
# 
# FileNotFoundError: Raised when a file or directory is requested but doesn’t exist.
# 
# IOError: Raised when an I/O operation (such as a print statement, the built-in open() function or a method of a file object) fails for an I/O-related reason.
# 
# ImportError: Raised when an import statement fails to find the module definition or when a from ... import fails to find a name that is to be imported.
# 
# MemoryError: Raised when an operation runs out of memory.
# 
# OverflowError: Raised when the result of an arithmetic operation is too large to be expressed by the normal number format.
# 
# AttributeError: Raised when an attribute reference or assignment fails.
# 
# SyntaxError: Raised when the parser encounters a syntax error.
# 
# IndentationError: Raised when there is incorrect indentation.
# 
# NameError: Raised when a local or global name is not found.

# 5. What is logging in Python, and why is it important in software development?
# 
# Logging is a technique for monitoring events that take place when some software is in use.
# For the creation, operation, and debugging of software, logging is crucial.
# It is important in software development because if your programme fails you would be able to identify the cause. 

# 6. Explain the purpose of log levels in Python logging and provide examples of when each log level would be appropriate.
# 
# A built-in Python package called logging enables publishing status messages to files or other output streams. The file may provide details about which portion of the code is run and any issues that have come up. There are different levels in logging - debug, info, warning, error and critical. It can be used to log according to the levels. The severity of the event being logged from least severe to most severe are debug, info, warning, error and critical. So, the other developers will be able to understand which one need to be handled first looking into the level.

# import logging
# 
# logging.basicConfig(level=logging.DEBUG)
# def div():
#     try:
#         a = int(input("Enter first number: "))
#         b= int(input("Enter second number: "))
#         logging.info("We are doing division")
#         logging.debug('Variables are %s and %s', a, b)
#         
#         div_result=a/b       
#          
#         return div_result
#     except ZeroDivisionError as e:
#         logging.error(e)
#         
#     except ValueError:
#         logging.warning("Please enter integer values only")
#         logging.critical("Looks like the user has entered string or float. Please enter valid numbers only")
#       
#     
# z = div()
# print("Division : ", z)
#    
# 

# 7. What are log formatters in Python logging, and how can you customise the log
# message format using formatters?
# We can set the format of the logs using a Formatter. This format includes the log timestamp, log level and log message. We can customise the log message format by using 
# 
# import logging
# logging.basicConfig(filename = "test.log", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
# 
# For example:

# import logging
# logging.basicConfig(filename = "test.log", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
# def div():
#     try:
#         a = int(input("Enter first number: "))
#         b= int(input("Enter second number: "))
#         logging.info("We are doing division")
#         logging.debug('Variables are %s and %s', a, b)
#         
#         div_result=a/b       
#          
#         return div_result
#     except ZeroDivisionError as e:
#         logging.error(e)
#         
#     except ValueError:
#         logging.warning("Please enter integer values only")
#         logging.critical("Looks like the user has entered string or float. Please enter valid numbers only")
#       
#     
# z = div()
# print("Division : ", z)

# 8. How can you set up logging to capture log messages from multiple modules or
# classes in a Python application?
# 
# We can capture log information by defining different modules in separate programs and then calling those modules in the main program.
# 
# For example:

# #test1.py
# 
# import logging
# import mylib
# 
# def main():
#     logging.basicConfig(filename='myapp.log', level=logging.INFO)
#     logging.info('Started')
#     mylib.def_anothermodule()
#     logging.info('Finished')
# 
# 
# main()

# #mylib.py
# import logging
# 
# def def_anothermodule():
#     logging.info('Capturing log information from multiple modules')

# Then run test.py program. It will create myapp.log which will have following :
# 
# INFO:root:Started
# INFO:root:Capturing log information from multiple modules
# INFO:root:Finished

# 9. What is the difference between the logging and print statements in Python? When
# should you use logging over print statements in a real-world application?
# 
# The print statement prints the message on the console but logging helps in recording the messages on to the file. 
# Python logging is a module that allows you to track events that occur while your program is running. You can use logging to record information about errors, warnings, and other events that occur during program execution. And logging is a useful tool for debugging, troubleshooting, and monitoring your program.

# 10. Write a Python program that logs a message to a file named "app.log" with the
# following requirements:
# ● The log message should be "Hello, World!"
# ● The log level should be set to "INFO."
# ● The log file should append new log entries without overwriting previous ones.

# import logging
# logging.basicConfig(filename="app.log", level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
# logging.info("Hello, world!")
# logging.info("Nice to meet you!!!")

# 11. Create a Python program that logs an error message to the console and a file named
# "errors.log" if an exception occurs during the program's execution. The error
# message should include the exception type and a timestamp.

# import logging
# logger = logging.getLogger()
# c_handler = logging.StreamHandler()
# f_handler = logging.FileHandler('error.log')
# c_handler.setLevel(logging.ERROR)
# f_handler.setLevel(logging.ERROR)
# c_format = logging.Formatter('%(asctime)s, %(message)s')
# f_format = logging.Formatter('%(asctime)s, %(message)s')
# c_handler.setFormatter(c_format)
# f_handler.setFormatter(f_format)
# logger.addHandler(c_handler)
# logger.addHandler(f_handler)
# 
# 
# def div():
#     try:
#         a = int(input("Enter first number: "))
#         b = int(input("Enter second number: "))
# 
#         div_result = a / b
# 
#         return div_result
#     except Exception as e:
#         logging.error(e)
# 
# 
# z = div()
# print("Division : ", z)
