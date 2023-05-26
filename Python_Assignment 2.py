#!/usr/bin/env python
# coding: utf-8

# 1.What are the two values of the Boolean data type? How do you write them?
# 
# True and False

# 2. What are the three different types of Boolean operators?
# 
# and, or and not

# 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
# 
#         and table               
#         
#               Output
#         F F     F
#         F T     F
#         T F     F
#         T T     T
#         
#         or table
#               Output 
#         F F     F
#         F T     T
#         T F     T
#         T T     T
#         
#         not table
#               Output       
#         F       T
#         T       F
# 

# 4. What are the values of the following expressions?

# (5 > 4) and (3 == 5)

# False

# not (5 > 4)

# False

# (5 > 4) or (3 == 5)

# True

# not ((5 > 4) or (3 == 5))

# False

# (True and True) and (True == False)

# False

# (not False) or (not True)

# True

# 5. What are the six comparison operators?

# < , > , == , <= , >= , !=

# 6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
# 
# The equal to (==) operator is a comparison operator. It comares thevalues on the right and left of the operator. If the values are eual , then it returns True, else it returns False.
# 
# The assignment operator (=) assigns the value to the variable.
# 
# Eg. 
# 
# n=0
# i=5
# while n<i:
#     if n==3:
#         print(n)
#     n = n+1
#        
#         
# In this example it checks whether the value of n is equal to (==)3. If its True then it will print the value of n, else it will print the value of n.
# 
# In this example initially variable n is assigned a value 0 (n=0) and variable i is assigned a value 5 (i=5).
#     
#         
#       

# 7. Identify the three blocks in this code:
# 
# spam = 0
# if spam == 10:
#     print('eggs')
# if spam > 5:
#     print('bacon')
# else:
#     print('ham')
#     print('spam')
#     print('spam')
# 
# 
# The three blocks are the if - else blocks including the print statements.

# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

# spam= int(input(" Enter a single digit integer value : "))
# 
# if spam == 1:
#     print("Hello")
# elif spam==2:
#     print("Howdy")
# else:
#     print("Greetings!")
#         
#     

# 9.If your programme is stuck in an endless loop, what keys you’ll press?
# 
# Ctrl C

# 10. How can you tell the difference between break and continue?
# 
# break and continue are reserved keywords. break takes the control out of the loop from a loop, while continue takes the control to the start of the loop.
# 

# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# 
# range(10)- It takes values from 0,1,2,3,4,5,6,7,8,9 excluding 10.
# range(0,10) - Its similar to range(10). Here the start point is 0 and endpoint is 9 excluding 10. (0,1,2,3,4,5,6,7,8,9)
# range(0,10,1)- startpoint is 0, endpoint is 10 excluding 10 and jump size is 1. (0,1,2,3,4,5,6,7,8,9)

# 12.Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
# 
# For loop
# 
# for i in range(1,11):
#     print(i)
#     
# 
# While loop
# 
# n=1
# i=10
# 
# while n<=i:
#     print(n)
#     n=n+1
# 
# 
# 
# 
# 

# 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
# 
# spam.bacon()
