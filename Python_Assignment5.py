#!/usr/bin/env python
# coding: utf-8

# 1. What does an empty dictionary's code look like?
# 
# {}

# 2. What is the value of a dictionary value with the key 'foo' and the value 42?
# 
# d= {foo':42}

# 3. What is the most significant distinction between a dictionary and a list?
# 
# Dictionary has unordered items and they are in the form of key:value pair while list have ordered items.

# 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
# 

# spam = {'bar': 100}

# spam['foo']

# Shows KeyError

# 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
# 
# 'cat' is generally taken as key. It checks for the value 'cat' in spam using spam.keys().

# 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
# 'cat' is generally taken as key. If spam.values(), it checks whether there is any key value having 'cat'.

# 7. What is a shortcut for the following code?
# 
# if 'color' not in spam:
# spam['color'] = 'black'
# 

# spam.setdefault('color', 'black')

# 8. How do you "pretty print" dictionary values using which module and function?
# 
# pprint.pprint()
#            
