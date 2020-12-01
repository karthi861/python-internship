#	List down all the error types and check all the errors using a python program for all errors

from math import cube       #import error

import cube         #module not found error

stud={1:"loey",2:"bbh",3:"kai"}
print(stud[4])      #key error

list1=[90,40,45]
print(list1[3])     #index error

marks=max(list1)
if marks<40:
    div=marks/0     #Zerodivision error
    print(div)
elif marks>40 | marks<80 :
    div=marks/2
    print(div)
else                #syntax error
    div=marks
    print(div)

print(name)         #name error

age=2
print('age'+2)      #type error

#print one message if the try block raises a NameError and another for other errors

try:
	a=5
	b=2
	sum=a+b
	print(sum)
	print(name,sum)
except NameError as ne:
	print("name error is caused",ne)
except Exception as e:
	print(e)

#Design a simple calculator app with try and except for all use cases

def add(a,b):
    c=a+b
    print(c)
def sub(a,b):
    c=a-b
    print(c)
def mul(a,b):
    c=a*b
    print(c)
def div(a,b):
   try:
    c=a/b
    print(c)
   except Exception as e:
       print("Exception caused:",e)


def enterinput():
    try:
        num1=int(input())
        num2=int(input())
        operator=input()
        if operator=='+':
           add(num1,num2)
        elif operator=='-':
            sub(num1,num2)
        elif operator == '*':
          mul(num1, num2)
        elif operator == '/':
             div(num1, num2)
        else:
              print("wrong input")
              enterinput()
    except Exception as e:
        print("Exception raised :",e)
    finally:
        enterinput()
enterinput()

#Try getting an input inside the try catch block

try:
    lst=[]
    n=int(input("Enter n:"))
    for i in range (0,n):
       value=int(input())
       lst.append(value)
    print(lst)
    print("enter index to be popped:")
    pop_ind=int(input())
    lst.pop(pop_ind)
    print(lst)
except Exception as e:
    print(e)

#When try-except scenario is not required?

When there is no exception in the code while running a program try-except block is not required
