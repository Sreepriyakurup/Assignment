#!/usr/bin/env python
# coding: utf-8

# Q.1. What are keywords in python? Using the keyword library, print all the python keywords.
# 
# Keywords are reserved words. We can't assign a value to the keyword.

# pip install keyword
# import keyword
# print (keyword.kwlist)
# 

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# Q.2. What are the rules to create variables in python?
# 
# Variables can be a combination of  alphabets (lower case a-z, upper case A-Z), digits, speial characters or underscore.      Non ASCII letters can also be used.
# Variables should not begin with digits or special characters. It should not contain space. Keywords cannot be used as variables. 

# Q.3. What are the standards and conventions followed for the nomenclature of variables in
# python to improve code readability and maintainability?
# 
# To improve the code readability and maintainability variables should be meaningful and of shorter length.
# To improve the readability comments are also written in the program. Single line comment starts with '#'. Multi line comments start with ''' (triple quotes) and end with '''.
# 
# Also multi line statements can be written using '\' symbol.

# Q.4. What will happen if a keyword is used as a variable name?

# It will show syntax error saying cannot asssign to keyword.

# Q.5. For what purpose def keyword is used?
# 
# def keyword is used to define or create a function.

# Q.6. What is the operation of this special character ‘\’?
# 
# We can extend a statement over multiple lines using special character '\'.

# Q.7. Give an example of the following conditions:
# (i) Homogeneous list
# (ii) Heterogeneous set
# (iii) Homogeneous tuple
# 
# (i) Homogenous list 
# [1,2,3,4,5]
# 
# (ii) Heterogeneous set
# {2,'cat',5,[1,6,7]}
# 
# (iii) Homogeneous tuple
# (9,8,7,6)

# Q.8. Explain the mutable and immutable data types with proper explanation & examples.
# 
# Mutable data types are those whose elements can be changed (added, removed, modified ) after they are created. Eg: list, set and dictionary.
# Eg: l = ['a','b','e','d']
# l[2] = 'c'
# print(l)
# 
# l= ['a','b','c','d']
# 
# Immutable data types are those whose elements cannot be changed (added, removed, modified ) after they are created. Eg: Strings and tuples.
# 
# Eg: t= ( 3,4,5,8,7)
# t[3] = 6
# print(t)
# 
# It will error out saying 'tuple' object does not support item assignment.

# Q.9. Write a code to create the given structure using only for loop.

# In[7]:


for i in range (1,10):
    if i%2 ==1:
        print (('*' * i).center(25, ' '))


# In[ ]:


Q.10. Write a code to create the given structure using while loop.


# In[11]:


i=10

while i>0:
    if i%2 ==1:
        print (('|' * i).center(25, ' '))
    i=i-1


# In[ ]:




