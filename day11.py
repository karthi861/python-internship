#Write a program using zip() function and list() function, create a merged list of tuples from the two lists given.

list1=["sm","jyp","yg","pledis"]
list2=["exo","got7","bp","svt"]

x=list(zip(list1,list2))
print(x)

#First create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples.

x=range(1,8)
list1=[4,2,7,6,1,10,11]
list2=list(zip(list1,x))
print(list2)

#Using sorted() function, sort the list in ascending order.

list1=["good","zip","noon","water","ant"]
list2=list(sorted(list1))
print(list2)

#Write a program using filter function, filter the even numbers so that only odd numbers are passed to the new list.
list1=[23,98,3,6,4,5,7,8,33,27,19,55,47,90]
list2=list(filter(lambda x:(x%2!=0),list1))
print("odd num:",list2)
