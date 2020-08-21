# def Delete(Friend):
#     Deletefriend=False
#     for i in range(len(Friend)-2):
#         if Friend[i]<Friend[i+1]:
#             Friend.pop(i)
#             Deletefriend=True
#             break
#     if Deletefriend==False:
#         Friend.pop(len(Friend)-1)
#     return Friend
        
        
# name = input() 
# print('Hi, %s.' % name) 
# inp=int(input())
# for i in range(inp):
#     howmanyfriende=input().split()
#     friendspopularitye=input().split()
#     friendspopularity=[]
#     for i in friendspopularitye:
#         friendspopularity.append(int(i))
        
#     for j in range(howmanyfriende[1]):
#         friendspopularity=Delete(friendspopularity)
#     for k in friendspopularity:
#         print(k,end=" ")
#     print()


# inp=int(input())
# list1=[list(map(int,input().split())) for i in range(inp)]
# sum,i=0,0
# while i<len(list1):
#     j=0
#     while j<len(list1): 
#         if i!=j: sum+=(abs(list1[i][0]-list1[j][0])+abs(list1[i][1]-list1[j][1]));
#         j+=1 ;           
#     list1.pop(0);
#     if len(list1)==1:break; 

        

# print(sum)



# for i in range(len(list1)):
#     for j in range(len(list1)):
#         if i!=j and list1[i]!=[] and list1[j]!=[]: sum+=(abs(list1[i][0]-list1[j][0])+abs(list1[i][1]-list1[j][1]));
#     list1.pop(i)
#     list1.insert(0,[])
#     if len(list1)==1:break; 
# print(sum)
# import itertools
# inp=int(input())
# list1=[list(map(int,input().split())) for i in itertools.islice(range(inp),inp)]
# list1=[(abs(list1[i][0]-list1[j][0])+abs(list1[i][1]-list1[j][1])) for i in itertools.islice(range(len(list1)),len(list1)) for j in itertools.islice(range(i,len(list1)),len(list1))]
# print(sum(list1))

# import string
# #Take an input string and determine if exactly 3 question marks exist between every pair of numbers that add up to 10. If so, print true, otherwise print false. Some examples of test cases are below:

# a="arrb6???4xxb15???eee5"
# b="ecc?7??sss?3rr1??????5"
# c="5??aaaaaaaaaa?5?5"
# d="9???1???9???1???9"
# e="aa6?9"
# f=0
# ff=0
# a=input()
# for i in range(len(a)):
# 	for j in range(len(a)):
# 		if i!=j :
# 			# print(string.digits)
# 			if a[i] in string.digits and a[j] in string.digits:
# 				if int(a[i])+int(a[j])==10:	
# 					q=a[i:j+1]
# 					print(q)
# 					for k in q:
# 						if k=="?":
# 							ff+=1
# 					if q:
# 						f+=1
# 						break
					
# if ff==(f)*3 and ff!=0:
# 	print(True)
# else:
# 	print(False)

# b=0
# for i in range(1000):
# 	for j in range(1000):
# 		if len(str(i))==3 and len(str(j))==3:
# 			a=str(i*j)
# 			if a==a[::-1] and int(b)<int(a):
# 				c,d=i,j
# 				b=a
# print(b,"=",c,"*",d)

import json
primelist=[2,3]
b=600851475143
# for i in range(3,b):
# 	print(i,end="\r")
# 	if b%i==0 :
# 		print(i,"devuser")
# 		flag=True
# 		for j in primelist:
# 			if i%j==0:
# 				flag=False
# 				break
# 		if flag:
# 			print(i)
# 			primelist.append(i)
# 			print(primelist)
# 			c=i		
import math

with open("primelist.json","r") as a:
	c=a.read()
	c=json.loads(c)
	c=json.loads(c)

primelist=c
for i in range(c[-1],b+1):
	flag=True
	for j in primelist:
		if  j>=math.sqrt(i):
			break
		if i%j==0:
			flag=False
			break
	if flag:
		primelist.append(i)
		print(i,end="\r")
	if i%100000==0:
		with open("primelist.json","w") as a:
			pl=json.dumps(primelist)
			json.dump(pl,a)
# print(c)



