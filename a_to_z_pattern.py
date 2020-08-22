
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
		for j in range(5):
			if j is 1 or (j is 4 and i >0 and i<6) or ((i is 0 or i is 6)and j !=4): 
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

t()
print("")
a()
print("")
r()
print("")
i()
print("")
q()
