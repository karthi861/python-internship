#	Write a program to create a list of n integer values and do the following
#1.	Add an item in to the list (using function)

>>>a = [1,2,3,4,5]
>>> a.append(6)
>>> a

[1, 2, 3, 4, 5, 6]

>>> a.insert(0,0)
>>> a

[0, 1, 2, 3, 4, 5, 6]

#2.Delete (using function)

>>>a = [1,2,3,4,5]
>>>a.pop(4)

4

>>> a.remove(0)
>>> a

[1, 2, 3, 5, 6]

#3.Store the largest number from the list to a variable

>>>a=[1,2,3,4,5]
>>> b = max(a)
>>> b

5

#4.Store the Smallest number from the list to a variable

>>>a=[1,2,3,4,5]
>>> b = min(a)
>>> b

1

#Create a tuple and print the reverse of the created tuple

>>>a= (1,2,3,4,5)
>>> b=tuple(reversed(a))
>>> print(b)

(5, 4, 3, 2, 1)

# Create a tuple and convert tuple into list

>>> a= (1,2,3,4,5)
>>> b=list(a)
>>> print(b)

[1, 2, 3, 4, 5]

