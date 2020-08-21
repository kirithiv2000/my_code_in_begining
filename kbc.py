# import pyttsx3
# engine = pyttsx3.init()
# engine.setProperty("rate",150)
# engine.setProperty("volume",0.5)


# print("-------Welcome to the KBC--------")
# engine.say("Welcome to the KBC game")
# engine.say("Hello Kirithiv How are you")
# engine.runAndWait()


# questions_=["which is the capital of India",
# "How many continents are there?",
# "What are you going to be?",
# "Which one of the following computers is the fastest, biggest and expensive computer?",
# "Which is the smallest continent? ",
# "Which acid is found in lemon? ",
# "What is India form of Governance? ",
# "which is the biggest continent? ",
# "How many states does India have? ",
# "How many union territories are there in india? "
# ]
# option_=[["1. Chandigarh", "2. Bhopal", "3. Chennai", "4. Delhi"],
# ["1. Four", "2. Nine", "3. Seven", "4. Eight"],
# ["1. Software Engineer", "2. Counseling", "3. Tourism", "4. Agriculture"],
# ["1. Personal Computer","2. Laptop","3. Netbook ","4. Super Computer"],
# ["1. Australia ","2. India ","3. Asia ","4. America "],
# ["1. Nitric Acid ","2. Citric acid","3. Sulfuric Acid ","4. Chloric Acid "],
# ["1. Authoritarianism ","2. Democracy ","3. Monarchy ","4. Oligarchy "],
# ["1. Australia ","2. India ","3. Asia ","4. America "],
# ["1. 30 ","2. 29 ","3. 07 ","4. 32 "],
# ["1. 30 ","2. 29 ","3. 07 ","4. 32 "]
# ]
# answer_=[4,3,1,4,1,2,2,3,2,3]
# l=len(questions_)
# a=0
# for i in questions_:
# 	print (i)
# 	engine.say(i)
# 	engine.runAndWait()
# 	for j in option_[a]:
# 		print (j)
# 		engine.say(j)
# 		engine.runAndWait()
# 	input_=input("Tell your answer 1 or 2 or 3 or 4\n")
# 	engine.say(input_)
# 	engine.runAndWait()
# 	if int(input_) is answer_[a]:
# 		print("congrats! your answer is correct")
# 		engine.say("congrats! your answer is correct")
# 		engine.runAndWait()
# 		a+=1
# 	else:
# 		print("sadly! your answer is wrong")
# 		engine.say("sadly! your answer is wrong")
# 		engine.runAndWait()
# 		break
