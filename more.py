########################questiion-1#####################
# for i in range(0,1001):
# 	if i%3==0:
# 		print("nav")
# 	elif i%7==0:
# 		print("gurukul")
# 	elif i%21==0:
# 		print("navgurukul")
# 	else:
# 		print(i)
########################question-2##########################
# noofstu=int(input("no of students"))
# expensesof1stu=int(input("expenses for 1 student aproximately"))
# if noofstu*expensesof1stu<50000:
# 	print("inside budget")
# if noofstu*expensesof1stu>50000:
# 	print("expenses are crossing budget")
##########################question-3#########################
# password=input("enter your password")
# if 6<len(password)<16:
# 	if "$" in password:
# 		if "2" or "8" in password:
# 			if "A" or "Z" in password :
# 				print("strong password")
# 			else:
# 				print("your password should contain A or Z")
# 		else:
# 			print("your password should contain  2 or 8")
# 	else:
# 		print("your password should contain a special character like $")
# else:
# 	print("your password should be more than 6letters and it should not exceed 15letters")
######################################################################question-4###########################################
# input1=int(input("enter a number"))
# input2=int(input("enter a number"))
# input3=int(input("enter a number"))
# if input1<input2<input3:
# 	print(input3,"is grater than all")
# if input1<input2>input3:
# 	print(input2,"is grater than all")
# if input1>input2>input3:
# 	print(input1,"is grater than all")
########################################################################quesstion-5######################################
# input1=int(input("enter a number"))
# b=1
# for i in range(1,input1+1):
# 	b*=i
# 	print(b)
#########################################################################question-6######################################
# string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
# new_list=[]
# for i in string_list:
# 	if i not in new_list:
# 		new_list.append(i)
# print(new_list)
##########################################################################question-7#####################################
# list1 = [1, 342, 75, 23, 98]
# list2 = [75, 23, 98, 12, 78, 10, 1]
# new_list=[]
# for i in list1:
# 	if i in list2:
# 		new_list.append(i)
# new_list.sort()
# print(new_list)
###########################################################################question-8#######################################
# list1 = [1, 5, 10, 12, 16, 20]
# list2 = [1, 2, 10, 13, 16]
# new_list=[]
# for i in list1:
# 	for j in list2:
# 		if i not in new_list:
# 			new_list.append(i)
# 		if j not in new_list:
# 			new_list.append(j)
# new_list.sort()
# print(new_list)
###########################################################################question-9##########################################
# for i in range(1,1001):
# 	a=list(str(i))
# 	add=0
# 	al=len(a)
# 	for j in range(0,al):
# 		add=add+int(a[j])
# 	if i%add==0:
# 		print(i)
###########################################################################question-10#############################################
# big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
# for i in range(0,len(big_list)):
# 	for j in range(0,len(big_list[i])):
# 		print (big_list[i][j])
# 	print("------------")

# marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
# for i in range(0,len(marks)):
# 	print (max(marks[i]))


###########################################################################question-11#############################################

# words = "navgurukul is great"
# counter = 0
# while counter < len(words):
#     print (words[counter])
#     counter+=1






