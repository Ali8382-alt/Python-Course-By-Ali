#Rule Based AI Python ChatBot 

import datetime
import time

name= input("well come , Enter your Name : ")
presentHour= datetime.datetime.now().hour

if 5 <= presentHour <= 11: 
    print("Good Morning, ", name)
elif 11 <= presentHour <= 17:
    print("Good Afternoon, ", name)
elif 17 <= presentHour <= 20:
    print("Good Evening, ", name)
else:
    print("Good Night, ", name)



print("AOA! Welcome to Your ChatBot")
print("You can ask me basic question, Type 'bye' to exit from the bot")

# Chatbot Memory Creation [ dictionary of responses ]

responses = {
    "hello": "Hi, welcome. How can I help you?",
    "how are you": "I am very fine. Thank you",
    "who are you": "I am smart AI chatbot",
    "motivate me": "Keep going. Every bug of your project makes you a better developer",
    "happy": "Great to hear that",
    "what are functions": "read chapter 7 "
} 

# Method/Function to get response of ChatBot 

def getResponseOfBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "I am not able to tell that yet. I Understand it very soon."    
    

# Take user input 


while True:
    userInput= input("Please ask your question:")
    reply= getResponseOfBot(userInput)
    print("Bot Response:", reply)

    if "bye" in userInput.lower():
        break
