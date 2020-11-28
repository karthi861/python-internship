#Write a program to loop through a list of numbers and add +2 to every value to elements in list
List1=[1,2,3,4,5]
For i in list1:
Print(i,i+2)

#Write a program to get the below pattern
#54321
#4321
#321
#21
#1
n=int(input("enter the num of pattern:"))
for i in range (n,0,-1):
 for a in range (1,i+1):
  print(a,end="")
 print()

#Python Program to Print the Fibonacci sequence

n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ")
while(count <= n):
  print(sum)
  count += 1
  a = b
  b = sum
  sum = a + b

#Explain Armstrong number and write a code with a function

num = int(input("Enter a number: "))  
sum = 0  
temp = num  
  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 3  
   temp //= 10  
  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number")

#Write a program to print the multiplication table of 9

For i in range(20):
Print(i*9)

#Check if a program is negative or positive

num = float(input("Enter a number: "))
if num >= 0:
   if num == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")

#Write a program to convert the number of days to ages

from datetime import date 
def calculateAge(birthDate): 
    days_in_year = 365.2425    
    age = int((date.today() - birthDate).days / days_in_year) 
    return age
print(calculateAge(date(2000, 11, 19)), "years")

#Solve Trigonometry problem using math function write a program to solve using math function

import math
x = 0.75 
print("math.cos(",x,"): ", math.cos(x));
print("math.sin(",x,"): ", math.sin(x));

#Create a calculator only on a code level by using if condition (Basic arithmetic calculation)

def add(num1, num2): 
    return num1 + num2 
def subtract(num1, num2): 
    return num1 - num2 
def multiply(num1, num2): 
    return num1 * num2 
def divide(num1, num2): 
    return num1 / num2 
print("Please select operation -\n" 
        "1. Add\n" 
        "2. Subtract\n" 
        "3. Multiply\n" 
        "4. Divide\n") 
select = int(input("Select operations form 1, 2, 3, 4 :")) 
number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 
if select == 1: 
    print(number_1, "+", number_2, "=", 
                    add(number_1, number_2)) 
elif select == 2: 
    print(number_1, "-", number_2, "=", 
                    subtract(number_1,number_2))
elif select == 3: 
    print(number_1, "*", number_2, "=", multiply(number_1,number_2))
elif select == 4: 
    print(number_1, "/", number_2, "=", 
                    divide(number_1, number_2)) 
else: 
    print("Invalid input")
