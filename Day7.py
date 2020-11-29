#Create a python module with list and import the module in another .py file and change the value in list

import example
example.add(4,5.5)


#Install pandas package (try to import the package in a python file

import pandas as pd
age=[15,24,45,50,75,100,8]
List=pd.Series(age)
print(List)


#Import sys package and find the python path

import sys
sys.path()


#Import a module that picks random number and write a program to fetch a random number from 1 to  100 on every run

import random
print("Printing random number using random.random()")
print(random.random())

#Try to install a package and uninstall a package using pip


pip install pandas #install pandas

pip uninstall pandas #uninstall pandas
