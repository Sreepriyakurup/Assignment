#!/usr/bin/env python
# coding: utf-8

# 1. What is a lambda function in Python, and how does it differ from a regular function?
# 
# Lambda functions are small, anonymous functions defined with the lambda keyword. They can take any number of arguments but can only have one expression. The arguments are not surrounded by parantheses as in regular function.
# 
# The Lambda function evaluates and returns only one value unlike in regular function.
# 
# Unlike in regular functions, Lambda functions do not require a return statement, the expression is implicitly returned.
# 
# 

# 2. Can a lambda function in Python have multiple arguments? If yes, how can you define and use
# them?
# 
# Yes, Lambda function can have multiple arguments. We can define them alongwith the lambda function in one line.
# Ex:
# sum = lambda a,b : a+b
# print(sum(5,2))
# 
# In this example a and b are the arguments. This can be used by using the variable sum alongwith the arguments.

# 3. How are lambda functions typically used in Python? Provide an example use case.
# 
# Lamda functions can be used to evaluate single expressions and also in in filter(), map(), reduce(), sorted(). 
# Eg: l=[1,2,3,4,5,6,7,8,9,10] 
# list(filter(lambda x: x % 2 == 0 , l))

# 4. What are the advantages and limitations of lambda functions compared to regular functions in
# Python?
# 
# Advantages
# 1. Lambda functions are anonymous functions so we do not have to name these functions.
# 2. The code is written in a single line and so it saves time and space. It improves the readability of the code.
# 3. Lambda functions are used as one of the parameters in map(), filter(), reduce() and sorted().
# 
# Limitations
# 1. If the logic is not simple, where we need to write many lines of code, its better not to use lambda functions. It will look complex.
# 2. They are useful for small tasks that are not reused throughout the code

# 5. Are lambda functions in Python able to access variables defined outside of their own scope?
# Explain with an example.
# 
# Lambda functions can access variables in their parameter list and the parameters in the global scope.
# Example for aceesing the variables in the global scope.

# n1=5
# n2=6
# add=lambda n1,n2:n1+n2
# print(add(n1,n2))

# Example for acccessing variables in the paramenter list
# 
# add=lambda n1,n2:n1+n2
# print(add(20,30))

# 6. Write a lambda function to calculate the square of a given number.

# square=lambda x: x**2
# print(square(26))

# 676

# 7. Create a lambda function to find the maximum value in a list of integers.

# l=[8,3,9,100,10,6]
# max_value = lambda x: max(l)
# print("Maximum value in the list is : ",max_value(l))

# Maximum value in the list is :  100

# 8. Implement a lambda function to filter out all the even numbers from a list of integers.

# l=[11,12,13,14,15,16,17,18,19,20]
# even_num = list(filter(lambda x : x % 2 == 0, l))
# print("Even numbers: ",even_num)

# Even numbers:  [12, 14, 16, 18, 20]

# 9. Write a lambda function to sort a list of strings in ascending order based on the length of each
# string.

# l=['aeiou','bcd','efgh','a','qrstuv', 'wx']
# 
# sort_list=list(sorted(l, key = lambda x : len(x)))
# print("Sorted List: ", sort_list)

# Sorted List:  ['a', 'wx', 'bcd', 'efgh', 'aeiou', 'qrstuv']

# 10. Create a lambda function that takes two lists as input and returns a new list containing the
# common elements between the two lists.

# 
# l1 =[i for i in input("Enter the first list items : ").split(',')]
# l2=[i for i in input("Enter the second list items : ").split(',')]
# 
# 
# l3= lambda l1,l2: [i for i in l1  if i in l2]
# print("Common elements present in both the lists are: ", l3(l1,l2))

# 11. Write a recursive function to calculate the factorial of a given positive integer.

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n * factorial(n-1)
# 
# result = factorial(4)
# print("Factorial is ",result )

# Factorial is  24

# 12. Implement a recursive function to compute the nth Fibonacci number.

# In[90]:


def fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        fibonacci_series=fibonacci(n-1)
        next_term=fibonacci_series[-1]+fibonacci_series[-2]
        fibonacci_series.append(next_term)
        return fibonacci_series
    
fibonacci_series_result=fibonacci(10)    
print(f"Fibonacci series is {fibonacci_series_result}")


# Fibonacci series is [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 13. Create a recursive function to find the sum of all the elements in a given list.

# l =[i for i in input("Enter the list: ").split(',')]
# n=len(l)
# 
# 
# def sum(n):
#     if n==0:
#         return int(0)
#     else:
#         return int(l[n-1])+ int(sum(n-1))
#        
#         
# result = sum(n)
# print("The size of the list is: ", n)
# print("Sum of all the elements in the list: ", result)

# Enter the list: 1,2,3,4,5,6,7,8,9,10
# The size of the list is:  10
# Sum of all the elements in the list:  55

# 14. Write a recursive function to determine whether a given string is a palindrome.

# s=input("Enter the string: ")
# 
# def palindrome(s):
#     if len(s)==0:
#         return True
#     else:
#         if s[0]==s[-1]:
#             return palindrome(s[1:-1])
#       
# result = palindrome(s)
# if result==True:
#     print(f"{s} is a Palindrome")
# else:
#     print(f"{s} is not a palindrome")
#         
#     

# Enter the string: malayalam
# malayalam is a Palindrome

# 15. Implement a recursive function to find the greatest common divisor (GCD) of two positive integers.

# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))
# 
# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b, a%b)
#     
# gcd_result=gcd(a,b)
# print(f"GCD of {a} and {b} is ",gcd_result)  
# 
#     

# Enter the first number: 54
# Enter the second number: 70
# GCD of 54 and 70 is  2

# In[ ]:




