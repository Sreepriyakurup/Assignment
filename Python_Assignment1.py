#!/usr/bin/env python
# coding: utf-8

# 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
# 
# *                      - expression
# 
# 'hello'                - value
# 
# -87.8                  - value
# 
# -                      - expression
# 
# /                      - expression
# 
# +	                   - expression 
# 
# 6                      -value
# 

# 2. What is the difference between string and variable?
# 
# String - It is a type of data that can be stored in a variable.
# variable - It is used to store the data.Eg: It can store integers, floating point numbers, strings etc.

# 3. Describe three different data types.
# 
# The three different data types are:
# 
# 1. Integer or int: Integers are whole numbers including 0, positive numbers or negatine numbers. Eg: 0, 10, -20
# 
# 2. Floating point or float: Floating point numbers are decimal values. Eg: 3.512
# 
# 3. String or str: String is a collection of one or more characters or digits put in single , double or triple quotes.
# 

# 4. What is an expression made up of? What do all expressions do?
# 
# Expression is a combination of variables, values and operators. Eg: c = a + 2*b + 100
# The expressions are evaluated by the python interpreter to produce the result.

# 5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
# 
# Expression is a combination of values, variables and operators while statement can be any instruction in the code that a python interpreter can execute. Expressions are statements too.
# 
# Eg: sum = 20+3*h   (Expression and statement)
# a = 10 (Assignment Statement)
# 

# 6. After running the following code, what does the variable bacon contain?

# In[1]:


bacon = 22
bacon + 1


# 7. What should the values of the following two terms be?

# In[2]:


'spam' + 'spamspam'


# In[3]:


'spam' * 3


# 8. Why is eggs a valid variable name while 100 is invalid?
# 
# Eggs is a valid variable name because it starts with an alphabet while 100 is invalid as it starts with a digit.

# 9. What three functions can be used to get the integer, floating-point number, or string version of a value?
# 
# Integer - int()
# Floating-point number - float()
# string - str()

# 10. Why does this expression cause an error? How can you fix it?
# 'I have eaten ' + 99 + ' burritos.'
# 
# The error is caused as a result of concatenating string data type with an integer.

# In[4]:


'I have eaten ' + ' 99 ' + ' burritos.'


# The error is rectified by converting integer data type (99) to string data type ('99').
