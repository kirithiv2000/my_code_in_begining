def a():
	for i in range(7):
		for j in range(5):
			if (j is 0 and 0<i ) or (i is 0 and (j!=4) and(j != 0)) or (i >0 and j is 4) or (i is 4)  :
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print("")	
def b():
	for i in range(7):
		for j in range(5):
			if (i is 0 and j is not 4) or (i is 3 and j is not 4) or(i is 6 and j is not 4) or (j is 0) or (j is 4 and i%3!=0) :
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print("")
def c():
	for i in range(7):
		for j in range(5):
			if (i is 0) or(i is 6) or (j is 0)  :
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print("")	
def d():
	for i in range(7):
		for j in range(4):
			if j is 0 or (j is 2 and i >0 and i<6) or ((i is 0 or i is 6)and j is 1): 
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print("")
def e():
	for i in range(7):
		for j in range(5):
			if (i is 0) or(i is 6) or (i is 3) or (j is 0)  :
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print("")	
def f():
	for i in range(7):
		for j in range(5):
			if (i is 0)  or (i is 3) or (j is 0)  :
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print("")
def g():
	for i in range(7):
		for j in range(5):
			if (i is 0) or(i is 6) or (i is 3 and j is not 1) or (j is 0) or (j is 4 and i >3)  :
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print("")
def h():
	for i in range(8):
		for j in range(5):
			if ((j is 0) or (i is 4)) or (j is 4):
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print()	
def i():
	for i in range(8):
		for j in range(5):
			if (i is 0) or ((i is 7) or (j is 2)):
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print()
def j():
	for i in range(7):
		for j in range(5):
			if (j is 2) or (i is 0) or (i is 6 and j < 2) or (i >3 and j is 0) :
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print("")
def k():
	for i in range(8):
		for j in range(5):
			if (j is 0) or ((i+j is 4) or (i-j is 3 )):
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print()
def l():
	for i in range(7):
		for j in range(5):
			if (j is 0) or (i is 6) :
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print("")
def m():
	for i in range(7):
		for j in range(5):
			if (j is 0) or (i is j and i<3) or (j is 4) or (j+i is 4 and i<3) :
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print("")		
def n():
	for i in range(5):
		for j in range(5):
			if ((j is 0) or (i is j)) or (j is 4):
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print()	
def o():
	for i in range(7):
		for j in range(5):
			if (i is 0) or(i is 6) or (j is 0) or (j is 4) :
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print("")	
def p():
	for j in range(8):
		for i in range(5):
			if ((j is 0) or (i is 0)) or((i is 4) and (j<4)) or ((j==3) and (j < 4)) :
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print()
def q():
	for i in range(9):
		for j in range(7):
			if (i is 0 and j < 4 and j >0) or(i is 6 and j < 4 and j >0) or (j is 0 and i <6 and i>0) or (j is 4 and i <6 and i>0) or (i-j==2 and j !=1 and j != 4 ) :
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print("")	
def r():
	for j in range(8):
		for i in range(5):
			if ((j is 0) or (i is 0)) or((i is 4) and (j<4)) or ((j==3) and (j < 4)) or (j-i ==3):
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print()
def s():
	for i in range(7):
		for j in range(5):
			if (i is 0) or(i is 6) or (i is 3) or (j is 0 and i<3) or (j is 4 and i>3)  :
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print("")	
def t():
	for i in range(8):
		for j in range(5):
			if (i is 0)  or (j is 2):
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print()
def u():
	for i in range(7):
		for j in range(5):
			if (j is 4) or(i is 6) or (j is 0)  :
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print("")	
def v():
	for i in range(5):
		for j in range(9):
			if ((i is j) or (i+j is 8)):
				print("*",end="")
			else:
				print("",end=" ")
		print()	
def w():
	for i in range(5):
		for j in range(18):
			if ((i is j) or (i+j is 8) or (j-i	 is 8) or (i+j is 16) ):
				print("*",end="")
			else:
				print("",end=" ")
		print()	
def x():
	for i in range(9):
		for j in range(9):
			if ((i is j) or (i+j is 8)):
				print("*",end="")
			else:
				print("",end=" ")
		print()	
def y():
	for i in range(9):
		for j in range(9):
			if ((i is j and i<5) or (i+j is 8 and i<5)) or (j is 4 and i>4) :
				print("*",end="")
			else:
				print("",end=" ")
		print()	
def z():
	for i in range(5):
		for j in range(5):
			if ((i is 0) or (i + j is 4)) or (i is 4):
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print()		

# r()
# print(" ")
# a()
# print(" ")
# h()
# print(" ")
# u()
# print(" ")

# l()
# l=[a(),b(),c(),d(),e(),f(),g(),h(),i()]


# def leap_year(a):
# 	b=0
# 	c=0
# 	l=[]
# 	while c<7:
# 		if a%4==0 and (a%100!=0 or a%400==0):
# 			# print(a)
# 			# print(b)
# 			b=a
# 		c+=1
# 		a+=1
		
# 	# print(b)
# 	m=b-4
# 	for i in range(3):
# 		l.append(m)
# 		m-=4
# 	n=b+4
# 	l.append(b)
# 	for i in range(3):
# 		l.append(n)
# 		n+=4
# 	for i in l:
# 		print (i)


# leap_year(a=int(input("enter any year")))

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

# lis=["tapas","pratik","tarique",]
# c=[]
# def re(b):
# 	for i in b:
# 		stror=i[::-1]
# 		c.append(stror)
# 	return(c)
# print(re(lis))

# c=0
# b=0
# a=[1,2,3,8]
# for i in range (0,len(a)):
# 	if a[i] <b:
# 		b=a[i]
# 	else :
# 		c=a[i]
# print(b)
# print(c)





