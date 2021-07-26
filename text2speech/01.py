import pyttsx3


data=input("Enter text for conversion to speech:")
engine=pyttsx3.init()  #variable will store the inital function of pyttsx3
engine.say(data)
engine.runAndWait()

