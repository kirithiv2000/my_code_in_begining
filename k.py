# speed = int(input("Gaadi ki speed daalo > ") )

# Ab aapne speed check kar ke kuch print karna hai:
# Agar 60 se kam hai toh print karna: "Speed kam hai"
# Agar 30 se kam hai toh print karna: "Speed bahot kam hai"
# Agar 100 se zyada hai toh print karo: "Bahot zyada hai"
# if speed > 50:
#     print ("Speed kam hai")
# elif speed < 30:
#     print ("Speed bahut kam hai")
# elif speed > 100:
#     print ("Speed bahut fast hai")
# else:
# 	print ("speed bahut kam hai")


# marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
# total_marks = 0
# counter = 0
# while counter < len(marks):
# 	marks = (total_marks +counter)
# 	counter = counter + 1
# 	print(marks)

             #7 tables


# a=0
# while a<100:
# 	if a%7==0:

# 		print(a)
# 		a+=7



#interview questions
 
# a=int(input ("enter number "))
# if a%10==0:
# 	print("fij buj")
# elif a%2==0:
# 	print("fij")
# elif a%5==0:
# 	print("buj")

# a=3
# while a<=100:
# 	if a%2==0:
# 		print(a)
# 	a+=1


# for i in range (1,100):
# 	for j in range (2,i):
# 		if j%i==0:
# 			break
# 	else:
# 		print(j)

#list1=[]
# import datetime
# print(datetime.datetime.now())
name=input("what is your name?\n\n\t")
family=input("how many family members in your family\n")
hobies=input("what are your favourate hobies\n")
navgurukul=input("how do u come to know about navgurukul \n")
place=input("where are you from?\n")
DOB=input("WHEN DID YOU born?\n")
aim=input("what is your aim in life\n")
status=input("according to you what is your situation poor/middle/rich?\n")
Months=input("how many Months you spend till now in navgurukul\n")
mobile=input("what is your mobile number\n")

a=open("te.txt","a")
# a.write("\n\n this interview was taken in the time of "+datetime)
a.write("\n\n\t there is a person in navgurukul his name is "+name+". His favourate hobies are "+hobies+".His mobile number is "+mobile+". there is "+family+" members in his family. he was got to know navgurukul with help of "+navgurukul+". he was from "+place+". he was born on "+DOB+".his aim was to "+aim+". He is from a "+status+" class family. He spend "+Months+"months in navgurukul")
a.close()

