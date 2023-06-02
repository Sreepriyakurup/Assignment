#!/usr/bin/env python
# coding: utf-8

# 1. What exactly is []?
# It is null list.It does not contain any items in the list.

# 2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)

# spam = [2, 4, 6, 8, 10]

# spam[2] = 'hello'
# spam

# [2, 4, 'hello', 8, 10]

# Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.

# spam = ['a', 'b', 'c', 'd']

# 3. What is the value of spam[int(int('3' * 2) / 11)]?

# spam[int(int('3' * 2) / 11)]

# 'd'

# 4. What is the value of spam[-1]?

# spam[-1]

# 'd'

# 5. What is the value of spam[:2]?

# spam[:2]

# ['a', 'b']

# Let's pretend bacon has the list [3.14, 'cat', 11, 'cat', True] for the next three questions.

# 6. What is the value of bacon.index('cat')?

# bacon = [3.14, 'cat', 11, 'cat', True]

# bacon.index('cat')

# 1

# 7. How does bacon.append(99) change the look of the list value in bacon?

# bacon.append(99)
# bacon

# [3.14, 'cat', 11, 'cat', True, 99]

# 8. How does bacon.remove('cat') change the look of the list in bacon?

# bacon.remove('cat')
# bacon

# [3.14, 11, True, 99]

# 9. What are the list concatenation and list replication operators?

# The list concatenation operator is '+' and list replication operator is '*'.

# 10. What is difference between the list methods append() and insert()?

# append() adds the item to the last of the list. But, we can add an item anywhere in the list using insert(). 

# 11. What are the two methods for removing items from a list?

# For removing items from a list we can use the function remove() or del satement.

# 12. Describe how list values and string values are identical.
# In both list and string,the slicing, replacing, inserting, concatenation and replication operations can be done.

# 13. What's the difference between tuples and lists?
# Lists are mutable (values can be changed, added or deleted) but tuples are immutable.
# In tuples data items are written in common brackets eg: t= (a,b,c,d) while in list , data items are written in square brackets eg:  l= [e,f,g,h]

# 14. How do you type a tuple value that only contains the integer 42?
# 
# (42)

# 15. How do you get a list value's tuple form? How do you get a tuple value's list form?
# 
# We can get a list value's tuple form using tuple() and get a tuple value's list form using list().

# 16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
# 
# Variables contain references to list values.

# 17. How do you distinguish between copy.copy() and copy.deepcopy()?
# The copy.copy() does a shallow copy while copy.deepcopy() is a copy process in which copy occurs recursively.
