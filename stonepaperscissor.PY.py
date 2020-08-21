import random
import getpass
game_list=["stone","paper","scissor"]
def player():
	print("you win "+computer1 + "-"+player1 + " you got ", p ," points")

def computer():
	print("you lost "+computer1+"-"+player1+" computer got ",c," points")



c=0
p=0
a=2
while c<a or p<a:
	computer1=random.choice(game_list)
	# print(computer1)
	player1=getpass.getpass("choose your stone/paper/scissor").lower()
	print("my choice - your choice")
	
	if computer1==player1:
		print("we both think same ("+player1+")")
		continue
	if computer1=="paper" and player1=="scissor":
		p+=1
		player()
	if computer1=="stone" and player1=="paper":
		p+=1
		player()
	if computer1=="scissor" and player1=="stone":
		p+=1
		player()	
	if computer1=="paper" and player1=="stone":
		c+=1
		computer()
	if computer1=="stone" and player1=="scissor":
		c+=1
		computer()
	if computer1=="scissor" and player1=="paper":
		c+=1
		computer()
	if p==a:
		print("user wins")
		n=input("do you want to play more press m or press any key to exit other than m ")
		if n=="m":
			a+=2
		else:
			break
	if c==a:
		print("user lost")
		n=input("do you want to play more press m or press any key to exit other than m ")
		if n=="m":
			a+=2
		else:
			break

		
else:
	print("thank you for playing")