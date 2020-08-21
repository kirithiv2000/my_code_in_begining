# ################################### FIRST QUESTION ###########################
# print "We will learn debugging by removing all the errors from this python file."
#_______________________________________________________________________________

# name = "NavGurukul"
# print name + ', ' +  str(year) + "mein start hua tha!"
#_______________________________________________________________________________

# price_milk = raw_input("1L milk ka price daalo?")
# print "10L milk " + str(int(price_milk)*10) + " rupees ka aata hai."
#_______________________________________________________________________________

# number = raw_input("please enter a decimal number")
# print "your number divided by 2 is equal to = " + str(int(number)/2)
#_______________________________________________________________________________

# mangoes = 5
# mangoes = mangoes + 5
# print mangoes / 5
#_______________________________________________________________________________

# speed = int( raw_input("Gaadi ki speed daalo > ") )
# if 29<speed < 60:
#     print "Speed kam hai"
# elif speed < 30:
#     print "Speed bahot kam hai"
# elif speed > 100:
#     print "Speed bahot fast hai"
#_______________________________________________________________________________
# day = raw_input("Aaj ka din kya hai? (monday/tuesday) > ")
# time = raw_input("Kaunse samay ka khana banana hai? (lunch/dinner) > ")
# if day == "tuesday" and time == "dinner":
#     print "Pav-Bhaji banegi aaj toh :)"
# elif day == "monday" or day == "tuesday":
#     print "Daal-Roti banegi aaj"
#_______________________________________________________________________________
# marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
# total_marks = 0
# counter = 0
# while counter < len(marks):
# 	total_marks = total_marks + int(marks[counter])
# 	counter = counter + 1
# print(total_marks)
#_______________________________________________________________________________
# def numbers_greater_than_twenty(num_list):
# 	counter = 0
# 	while counter < len(num_list):
# 		item = num_list[counter]
# 		if item > 20:
# 			num_list.remove(item)
# 		counter+=1
# 	return num_list

# num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
# print "Initial list", num_list
# num_list_20 = numbers_greater_than_twenty(num_list)
# print "List that doesn't contain numbers greate than 20", num_list_20
#_______________________________________________________________________________
# from random import randint

# def win():
#     print 'You win!'

# def lose():
#     print 'You lose!'

# while True:
#     player_choice = raw_input('What do you pick? (rock, paper, scissors)')
#     player_choice.strip()
#     random_move = randint(0, 2)
#     moves = ['rock', 'paper', 'scissors']
#     computer_choice = moves[random_move]

#     if player_choice == computer_choice:
#         print 'Draw!'
#     elif player_choice == 'rock' and computer_choice == 'scissors':
#         win()
#     elif player_choice == 'paper' and computer_choice == 'scissors':
#         lose()
#     elif player_choice == 'scissors' and computer_choice == 'paper':
#         win()
#     elif player_choice == 'scissors' and computer_choice == 'rock':
#         lose()
#     elif player_choice == 'paper' and computer_choice == 'rock':
#         win()
#     elif player_choice == 'rock' and computer_choice == 'paper':
#         lose()
#     again = raw_input('Do you want to play again? (y or n)').strip()
#     if again == 'n':
#         break
#_______________________________________________________________________________
# chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

# # encrypt_message function defined here but not called
# def encrypt_message(plain_msg):
# # this fucnction takes "plain_msg" as an argument and print/return the encrypted message. The "plain_msg" is tranfered into "encrypted_msg" using "shifted_chars" list. Example, if plain_msg = "ng" then n => p, g => i  and hence encrypted_msg = "pi"
#     encrypted_msg = ""
#     for character in plain_msg:
#       # for character in msg
#         if character in chars:
#             char_index = chars.index(character)
#             new_char = shifted_chars[char_index]
#             encrypted_msg = encrypted_msg + new_char
#         else:
#             encrypted_msg = encrypted_msg + character
#     return encrypted_msg

# # decrypt_message function defined here but not called
# def decrypt_message(encrypted_msg):
# # this fucnction takes "encrypted_msg" as an argument and print/return the encrypted message. The "encrypted_msg" is tranfered into "decrypted_msg" using "shifted_chars" list. Example, if encrypted_msg = "pi" then p => n, i => g  and hence decrypted_msg = "ng"
#     decrypted_msg = ""
#     for character in encrypted_msg:
#         if character in shifted_chars:
#             char_index =  shifted_chars.index(character)
#             new_char = chars[char_index]
#             decrypted_msg = decrypted_msg + new_char
#         else:
#             decrypted_msg = decrypted_msg + character
#     return decrypted_msg


# # methods should return or print the new messages.
# ############################################### Code starts from here ##################################################
# flag = True
# while flag == True:
# 	choice = raw_input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!")
# 	if choice == 'e':
# 	    plain_message = raw_input("Enter message to encrypt??")
# 	    print(encrypt_message(plain_message))
# 	elif choice == 'd':
# 	    encrypted_msg = raw_input("Enter message to decrypt?")
# 	    print(decrypt_message(encrypted_msg))
# 	else:
# 	    play_again = raw_input("Do you want to try agian or Do you want to exit? (Y/N)").upper()
# 	    if play_again == 'Y':
# 	        continue
# 	    elif play_again == 'N':
# 	        break

#_______________________________________________________________________________

# from random import randint # allows you to generate a random number

# # variables for the alien
# alive = True
# stamina = 10

# # this function runs each time you attack the alien
# def report(stamin):
# # syntactic error in if else statements
# 	if stamin > 8:
# 		print "The alien is strong! It resists your pathetic attack!"
# 	elif stamin > 5:
# 		print "With a loud grunt, the alien stands firm."
# 	elif stamin > 3:
# 		print "Your attack seems to be having an effect! The alien stumbles!"
# 	elif stamin > 0:
# 		print "The alien is certain to fall soon! It staggers and reels!"
# 	else:
# 		print "That's it! The alien is finished!"

# # main function - accepts your input for fight with the alien
# def fight(stam): # stamina
#     while stam > 0:
#       # won't enter this loop ever. The function will always return False.
#         response = raw_input("> Enter a move 1.Hit 2.attack 3.fight 4.run")
#         # chose a response from ( hit, attack, fight and run)
#         # fight scene
#         if "hit" in response or "attack" in response:
#             less = randint(0, stam)
#             stam -= less # subtract random int from stamina
#             report(stam) # see function above
#         elif "fight" in response:
#             print "Fight how? You have no weapons, silly space traveler!"
#         elif "run" in response:
#             print "Sadly, there is nowhere to run.",
#             print "The spaceship is not very big."
#         else:
#             print "The alien zaps you with its powerful ray gun!"
#             return True
#     return False

# print "A threatening alien wants to fight you!\n"
# # quotes at the end.

# # call the function - what it returns will be the value of alive
# alive = fight(stamina)

# if alive: # means if alive == True
#     print "\nThe alien lives on, and you, sadly, do not.\n"
# else:
#     print "\nThe alien has been vanquished. Good work!\n"

#_______________________________________________________________________________

# chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# def ord(char):
# 	ind_=chars.index(char)
# 	ind_+=97
# 	return ind_

# def chr(num):
# 	num-=97
# 	alp=chars[num]
# 	return alp

# def encrypt():
# 	message = raw_input("Enter the message you want to encrypt").lower()
# 	ascii_message = [ord(char)+3 for char in message]
# 	encrypt_message = [ chr(char) for char in ascii_message]  
# 	print ''.join(encrypt_message)


# def decrypt():
# 	message = raw_input("Enter the message you want to decrypt").lower()
# 	ascii_message = [ord(char)-3 for char in message]
# 	decrypt_message = [ chr(char) for char in ascii_message]  
# 	print ''.join(decrypt_message)

# flag = True
# while flag == True:
# 	choice = raw_input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively!").lower()
# 	if choice == 'e':
# 		encrypt()
# 	elif choice == 'd':
# 		decrypt()    
# 	else:
# 		play_again = raw_input("Do you want to try agian or Do you want to exit? (Y/N)").upper()
# 		if play_again == 'Y':
# 			continue
# 		elif play_again == 'N':
# 			break
#_______________________________________________________________________________

# import random
# def getSecretNum(numDigits):
# # Returns a string that is numDigits long, made up of unique random digits.
# 	numbers = list(range(10))
# 	random.shuffle(numbers)
# 	secretNum = ''
# 	for i in range(numDigits):
# 		secretNum += str(numbers[i])
# 	return (secretNum)

# def getClues(guess, secretNum):
# # Returns a string with the pico, fermi, None clues to the user.
# 	if guess == secretNum:
# 		return 'You got it!'

# 	clue = []
# 	for i in range(len(guess)):
# 		if guess[i] == secretNum[i]:
# 			clue.append('Fermi')
# 		elif guess[i] in secretNum:
# 			clue.append('Pico')
# 		else:
# 			clue.append('None')
# 	return ' '.join(clue)

# def isOnlyDigits(num):
# # Returns True if num is a string made up only of digits. Otherwise returns False.
# 	if num == '':
# 		return False

# 	for i in num:
# 		if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
# 			return True
# 	return False

# def playAgain():
# # This function returns True if the player wants to play again, otherwise it returns False.
# 	play = raw_input("Do you want to play again? Yes or No?").lower()
# 	if play[0]=='y' :
# 		return True
# 	return False

# NUMDIGITS = 3
# MAXGUESS = 10

# print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
# print('Here are some clues:')
# print('When I say:    That means:')
# print('  Pico         One digit is correct but in the wrong position.')
# print('  Fermi        One digit is correct and in the right position.')
# print('  None       No digit is correct.')

# while True:
# 	secretNum = getSecretNum(NUMDIGITS)
# 	print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))
# 	numGuesses = 1
# 	while numGuesses <= MAXGUESS:
# 		print 'Guess' + str(numGuesses)
# 		guess = (raw_input("Guess The Number >>>"))
# 		while len(guess) == NUMDIGITS and not isOnlyDigits(guess):
# 			clue = getClues(guess, secretNum)
# 			print(clue)
# 			break
# 		if guess == secretNum:
# 			numGuesses=10
# 		numGuesses += 1
# 	if numGuesses > MAXGUESS:
# 		print 'You ran out of guesses. The answer was ' + secretNum
# 		if not playAgain():
# 			break
#_______________________________________________________________________________

# import json
# with open('users.json') as data_file:    
#     data = json.load(data_file)

# users = data['users']

# for user in users:
# 	counter = 0
# 	print "users full name is " + user['firstName'] + ' ' + user['lastName']
# 	while counter < 1:
# 		print "users mobile number is " + str(user['details']['mobileNo'])
# 		print "users age  is " + str(user['details']['age'])
# 		print "users city is " + user['details']['City']
# 		counter+=1
#_______________________________________________________________________________

