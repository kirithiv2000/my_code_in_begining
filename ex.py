# lis=int[23,34,52,67,890]
# a=len(lis)
# b=0
# d=0
# while b < a:
# 	d=b+
# 	print (b)
# 	d+=1 


# lis=[23,34,52,67,890]
# a=0
# for i in lis:
# 	a+=i
# print(a)


# a=[23,34,56,78]
# b=0
# c=0
# while b<len(a):
# 	c+=(a[b])
# 	b+=1
# print (c)
#  

# a=[23,6,6,78]
# b=0
# c=1
# while b<len(a):
# 	print (len(a))
# 	c*=(a[b])
# 	print (c)
# 	b+=1



# user=int(input("entre"))
# b=int(input("enter"))
# var=1
# v=0
# while var<user:
# 	v=v+b
# 	var+=1
# 	print(v)




# import random
# a=random.randint(0,20)
# print(a)


 


# l=[]
# a=0
# c=0
# print("enter ten friends name\t")
# while a<10:
# 	b=input("enter name")
# 	print (b)
# 	l=insert(1,b)
# 	print(l)
# 	a+=1
# # print(l)
# for i in l:
# 	print(i)




# k and people#only with numbers	
	# print (s)
	# print (q)
# l=[]
# j=[]
# import random
# a=0
# print("enter 10 people")


# while a<7:
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
# 		s.insert(100,k)
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


                           # without using another enpty list
# l=[]
# j=[]
# import random
# a=0
# print("enter 10 people")

# while a<7:
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
# while a<7:
# 	k=random.choice(l)
# 	m=random.choice(j)
# 	l.remove(k)
# 	j.remove(m)
# 	print(k,"is i

# for i in range (1,100):
# 	for j in range (2,i):
# 		if j%i==0:
# 			break
# 		else:
# 			print(i)ncharge to",m ,"today")
# 	a+=1

# import random 
# a=random.randint(1,10)
  
# # using random() to generate a random number 
# # between 0 and 1 
# print ("A random number between 1 and 10 is : "a) 




# import pyttsx3
# engine = pyttsx3.init()
# engine.setProperty("rate",0)
# engine.setProperty("volume",10)

# sudo set-sink volume -0 -10 or +10



# engine.say("I am your linux assistant.... how can I help you?")
# engine.runAndWait()



# import speech_recognition as sr
# import webbrowser as wb 
# chrome_path='/home/practice/Desktop'
# r=sr.Recognizer()
# with sr.Microphone() as source:
# 	print("say something!")
# 	audio=r.listen(source)
# 	print("done")



# try:
# 	text=r.recoganize_google(audio)
# 	print('Google thinks you said:\n'+ text)

# except Exception as e:
# 	print(e) 


# import speech_recognition       
# import pyttsx3


# speech_engine = pyttsx3.init('sapi5') # see         
# speech_engine.setProperty('rate', 150)


# def speak(text):
#    speech_engine.say(text)
#    speech_engine.runAndWait()

# recognizer = speech_recognition.Recognizer()



# def listen():
#     with speech_recognition.Microphone() as source:
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)

#     try:
#         return recognizer.recognize_sphinx(audio) 
#         # or: return recognizer.recognize_google(audio)
#     except speech_recognition.UnknownValueError:
#         print("Could not understand audio")
#     except speech_recognition.RequestError as e:
#         print("Recog Error; {0}".format(e))

#     return ""










# speak("Say something!")
# speak("I heard you say 

# for i in range (1,100):
# 	for j in range (2,i):
# 		if j%i==0:
# 			break















# 		else:
# 			print(i)" + listen())




# a=["ram","rita"]
# a.remove("ram")
# print(a)




# lis=[23,34,56,78]
# lit=[2,4,8,7,]
# c=0
# b=0
# d=0
# a=0
# for i in lis:
# 	b+=i
# print(b)
# for j in lit:
# 	c+=j
# 	d=c+b

# print(d)



