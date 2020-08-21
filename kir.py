# a=raw_input("entr")
# a=0
# b=0
# c=0
# for j in a:
# 	if a.isdigit():
# 		a+=1
# 	if c==1

# a=input("enter")
# b=0
# c=0
# while b<a:
# 	b+=1
# 	c*=a
# 	print(a)

# for i in range(6):
# 	for j in range(0,i):
# 			print("*",end="")
# 	else:
# 		print()


# for i in range(5,0,-1):
# 	for j in range(i): 
# 			print("*",end="")
# 	else:
# 		print()


#luckey corner
# print ("Today we will check this is your luckey day ")
# import random
# b=0
# while b<5:
# 	l=random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
# 	print l
# 	a=raw_input("enter any alphabet")
# 	if a is l:
# 		print("Today is your luckey day")
# 		break
# 	else:
# 		print("Try another time")
# 		print("Today is not your luckey day")

# 					#
# l=[]
# a=0
# print("enter ten friends name\t")
# while a<10:
# 	b=input("enter name")
# 	print (b)
# 	l.insert(100,b)
# 	a+=1
# # print(l)
# for i in l:
# 	print(i)


# work and people#only with numbers	
	# print (s)
	# print (q)
# l=[]
# j=[]
# import random
# a=0
# print("enter 10 people")

# while a<10:
# 	b=input("enter name\n\t")
# 	# print (b)
# 	l.insert(10,b)
# 	a+=1
# print(l)
# print("enter 10 works you want to do")
# while a>0:
# 	d=input("enter works\v")
# 	j.insert(10,d)
# 	a-=1
# print(j)
# s=[]
# q=[]
# while a<1000:
# 	k=random.choice(l)
# 	m=random.choice(j)
# 	if k in s or m in q:
# 		continue
# 	else:
# 		s.insert(10++0,k)
# 		q.insert(100,m)
# 		print(k,"is incharge to",m ,"today")
# 		a+=1

# mentees and mentors
# l=[]
# j=[]
# import random
# a=0
# print("enter 10 mentors name")

# while a<10:
# 	b=input("enter name\n\t")
# 	# print (b)
# 	l.insert(100,b)
# 	a+=1
# print(l)
# print("enter 10 mentees name")
# while a>0:
# 	d=input("enter name\v")
# 	j.insert(100,d)
# 	a-=1
# print(j)
# s=[]
# q=[]
# while a<100:
# 	k=random.choice(l)
# 	m=random.choice(j)
# 	print (s)
# 	print (q)
# 	if k in s:
# 		continue
# 	if m in q:
# 		continue
# 	if (k not in s) and (m not in q) :
# 		s.insert(100,k)
# 		q.insert(100,m)
# 		print(k,"is mentor of ",m ,"today")
# 	a+=1


                           #without using another enpty list
# l=[]
# j=[]
# import random
# a=0
# print("enter 10 people")

# while a<10:
# 	b=input("enter name\n\t")
# 	l.insert(10,b)
# 	a+=1
# print(l)
# print("enter 10 works you want to do")
# while a>0:
# 	d=input("enter works\v")
# 	j.insert(10,d)
# 	a-=1
# print(j)
# while a<10:
# 	k=random.choice(l)
# 	m=random.choice(j)
# 	l.remove(k)
# 	j.remove(m)
# 	print(k,"is incharge to",m ,"today")
# 	a+=1



# a=list(range(10))
# print(a)
# A=list(i for i in range(10,20,2))
# print(A)
# string_with_comas="hi,hello,how are you?,i am fine?,i love you"
# stringlst=string_with_comas.split(',')
# print(stringlst)
# a="hello"
# alst=list(a)
# print(alst)
# my_dict={"a":1,"b":2,"c":3,"d":4}
# key_list=list(my_dict.keys())
# print(key_list)
# value_list=list(my_dict.values())
# print(value_list)
# a=[1,2,3,4,5,6,8,9,"a","c"]
# print(a)
# bindex=a.index('a')
# print(bindex)
# a.insert(bindex+1,"b")
# print(a)
# index6=a.index(6)
# print(index6)
# a.insert(index6+1,7)
# print(a)
# popped=a.pop()
# print(popped)
# popped1=a.pop(1)
# print(popped1)
# a.reverse()
# print(a)
# A=[1,2,3,4,5,6,7,8,9]
# print(A[0:3])
# print(A[0:5:2])


# S=A[::-1]#slicing
# print(S)

# A[9:9]=[10,11]
# print(A)
# A[0:2]=[10,11]
# print(A)
# A[0:2]=[1,2]
# print(A)
# a=[1,2,3,4]#list
# print(a)
# b=list(a)
# print(b)
# a[0]=4
# print(a)
# print(b)
# a=[[1,2,3],[4,5],[6]]#nested list
# print(a)
# b=list(a)
# print(b)
# a[0][0]=4
# print(a)
# print(b)

# print(a)
# import copy
# b=copy.deepcopy(a)
# print(b)
# a[0][0]=4
# print(a)
# print(b)
# for i in a:
# 	print(i)

# a=["cat","dog","duck","jack"]
# for i in range(0,len(a)):
# 	print("index :",i,"|value :",a[i])
# 	print("index :"+str(i)+"| value :"+a[i])

# a=["hello","world!!","python","is","awesome"]#join string in list
# astr=" ".join(a)
# print(astr)
# astr2="-".join(a)
# print(astr2)


# listoflist=[[1,2],[5],[3,4]]
# print(listoflist)
# import itertools
# flat_list=list(itertools.chain(*listoflist))
# print(flat_list)

# lst=[1,1,2,3,3,4,5,5,6,6,6]
# print(lst)
# lst2=[i for i in lst if lst.count(i)>1]
# print(lst2)
# unique=set(lst2)
# print(unique)

# lst2=[1,2,3]
# print(lst2)
# from collections import deque
# lst2 = deque(lst2)
# print(lst2)
# lst2.rotate(2)
# print(lst2)

# saral
# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]

# print len(students)
# print len(marks)

# length = len(students) # kyunki dono ki same length hai toh jiski bhi length le sakte ho
# counter = 0
# while counter < length:
# 	print students[counter]+"'s mark is " + str(marks[counter])
# 	counter+=1

# list_ = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# len1=len(list_)
# c=[]
# for i in range (0,len1):
# 	if list_[i] in list2:
# 		continue
# 	else:
# 		c.append(list_[i])
# print(c)


# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# a=0
# l=len(elements)
# c=0
# d=0
# while a<l:
# 	if elements[a]%2 is 0:
# 		c+=1
# 	else:
# 		d+=1
# 	a+=1
# print(c," even numbers")
# print(d," odd numbers")

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# a=0
# l=len(elements)
# c=0
# d=0
# while a<l:
# 	if elements[a]%2 is 0:
# 		c+=elements[a]
# 	else:
# 		d+=elements[a]
# 	a+=1
# print(c," even numbers")
# print(d," odd numbers")

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# a=0
# l=len(elements)
# c=0
# C=0
# d=0
# D=0
# while a<l:
# 	if elements[a]%2 is 0:
# 		c+=elements[a]
# 		C+=1
# 	else:
# 		d+=elements[a]
# 		D+=1
# 	a+=1
# print(c," even numbers")
# print(d," odd numbers")
# print(C," EVEN")
# print(D," odd")
# print(c/C ," IS AVERAGE OF EVEN numbers")
# print(d/D," IS AVERAGE OF EVEN numbers")
# print((c+d)/(l-1)," is overall average")

# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# g=set(n)
# print(list(g))

# mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# subStr = "over"
# replacementStr = "on"
# l=mainStr.split(" ")
# print(l)
# c=l.count(subStr)
# a=0
# while a<c:
# 	if subStr in mainStr:
# 		m=l.index(subStr)
# 		l[m]="on"
# 		a+=1
# s=" ".join(l)
# print(s)



# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# unigue=set(char_list)
# u=list(unigue)
# print(u)
# l=len(unigue)
# a=0
# A=[]
# while a<l:
# 	c=char_list.count(u[a])
# 	print (u[a]+" is  " + str(c)+" times")
# 	aa=[u[a],c]
# 	A.insert(l-1,aa)
# 	a+=1
# print(A)

# diwale=0
# lakhpathi=0
# crorepathi=0
# kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
# k=kitna_paisa_hai
# for i in kitna_paisa_hai:
# 	l=len(str(i))
# 	if l<5:
# 		diwale+=1
# 	if l>=5 and l<8:
# 		lakhpathi+=1
# 	if l>=8:
# 		crorepathi+=1
# print ("Diwale :",diwale)
# print ("Lakhpathi :",lakhpathi)
# print ("Crorepathi :",crorepathi)

# list_=[10, 11, 12, 13, 14, 17, 18, 19]
# len1=len(list_)
# a=30
# c=[]
# d=[]
# for i in range (0,len1):
# 	for j in range(0,len1):
# 		if (list_[i] + list_[j] is a) and ((list_[i] not in d) or (list_[j] not in d)) :
# 			if list_[i] != list_[j] :
# 				g=[]
# 				d.append(list_[i])
# 				d.append(list_[j])
# 				g.append([list_[i],list_[j]])
# 				print(g)
# 				c.append(g)
# 			else:
# 				continue
# 		else:
# 			continue
# print(c)



# def menu(day):
#     if day == "monday":
#         food = "Butter Chicken"
#     elif day == "tuesday":
#         food = "Mutton Chaap"
#     else:
#         food = "Chole Bhature"
#     print "Kya main print ho payungi? :-("
#     return food
#     print "Lekin main toh pakka nahi print hounga (:'("



# def menu(day):
#     if day == "monday":
#         return "Butter Chicken"
#     elif day == "tuesday":
#         return "Mutton Chaap"
#     else:
#         return "Chole Bhature"

#     print "Kya main print how payungi? :-("

# mon_menu = menu("monday")
# print mon_menu
# tues_menu = menu("tuesday")
# print tues_menu
# fri_menu = menu("friday")
# print fri_menu

# menu("tuesday")
# print(menu("tuesday"))

# def a(n1,n2,c):
# 	if c=="add":
# 		add=n1+n2
# 		return(add)
# 	if c=="sub":
# 		sub=n1-n2
# 		return(sub)
# 	if c=="mul":
# 		mul=n1*n2
# 		return(mul)
# 	if c=="div":
# 		div=n1/n2
# 		return(div)
# print()
# number1= a(24,20,"add")
# print()
# number2=a(50,60,"mul") 
# print()
# number3= a(80,120,"div")
# print()
# number4= a(90,23,"sub")
# print(number4)
# print(number3)
# print(number2)
# print(number1)



# a=int(input("enter first number"))
# b=int(input("enter second number"))
# add_result=(a+b)
# subtract_result=(a-b)
# multiply_result=(a*b)
# divide_result=(a/b)
# print(add_result,subtract_result,multiply_result,divide_result)


# s=[1,2,3,4]
# a=[4,3,2,1]
# v=[]
# mul=[a,s]
# if len(s)==len(a):
# 	for i in range(0,len(a)):
# 		mult=s[i]*a[i]
# 		v.append(mult)
# print(v)

# a=[2, 6, 18, 10, 3, 75]
# b=[6, 19, 24, 12, 3, 87]
# if len(a)==len(b):
# 	for i in range (0,len(a)):
# 		if a[i] % 2==0 and b[i]%2==0:
# 			print("both are even")
# 			print("-----------------")
# 		else:
# 			print("both are not even")
# 			print("-----------------")


# expendture=[]
# money1=[]
# instudents=int(input("how many types of expendture"))
# for i in range(0,instudents):
# 	name=input("enter name of the expendture like daily milk/food/monthly rent/etc,...\n")
# 	expendture.append(name)
# 	money=int(input("enter amount of expendture of "+name))
# 	money1.append(money)
# print(sum(money1))
# if sum(money1)<50000:
# 	print("budjet is less than 50,000")
# else:
# 	print("budjet is more than 50,000")





	



