#Write a Python script to merge two Python dictionaries
>>>mobiles = {"1g":"oppo","2g" : "honor","3g":"samsung"}
>>>new = {"4g":"lenovo","5g":"oneplus"}
>>>mobiles.update(new)
>>>print(mobiles)

{'1g': 'oppo', '2g': 'honor', '3g': 'samsung', '4g': 'lenovo', '5g': 'oneplus'}

#Write a Python program to remove a key from a dictionary
>>>mobiles = {"1g":"oppo","2g" : "honor","3g":"samsung"}
>>>mobiles.pop("1g")
>>>print(mobiles)

{'2g': 'honor', '3g': 'samsung'}

#Write a Python program to map two lists into a dictionary
>>>mobiles = ("oppo","honor","samsung")
>>>type = ("1g","2g","3g")
>>>rate = dict(zip(mobiles,type))
>>>print(rate)

{'oppo': '1g', 'honor': '2g', 'samsung': '3g'}

#Write a Python program to find the length of a set

>>>new = {"lenovo","oneplus"}
>>>print(len(new))

2

#Write a Python program to remove the intersection of a 2nd set from the 1st set

>>>mobiles = {"samsung","oppo", "lenovo"}
>>>new ={"honor","vivo","lenovo"}
>>>c = mobiles&new
>>>print(c)

'lenovo'
