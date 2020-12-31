print("If you got any problem please email me adhul9090@gmail.com")

import pyttsx3
engine = pyttsx3.init()
import wikipedia

print("This program is still under developing some new feautures will available in next version some feautures are update checker,sapi5 voice.")
user=input("How can i help you: ")
engine.say(user)

print(user)

engine.say("Searching in wikipedia")

print("Searching in wikipedia")

result=print(wikipedia.summary(user))

engine.say(wikipedia.summary(user))
engine.runAndWait() 
