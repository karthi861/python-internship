#Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

import re
def char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)
print(char("PONvizhi19")) 
print(char("ponvizhi@2k"))


#Write a Python program that matches a word containing 'ab'.

import re
def match(text):
        patterns = '\w*ab.\w*'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(match("I went to abroad last week."))
print(match("Python Internship."))


#Write a Python program to check for a number at the end of a word/sentence.

import re
def match(text):
        patterns = '\w+\S *4'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(match("karthi154"))
print(match("karthi100"))
print(match("154karthi"))


#Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string

import re
results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 34995 are important")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))


#Write a Python program to match a string that contains only uppercase letters

import re
def text_match(text):
        patterns = '^[A-Z]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("KARTHI"))
print(text_match("karthi_18"))


 
