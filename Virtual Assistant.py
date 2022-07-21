#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import speech_recognition as sr
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser
from PIL import Image, ImageTk
from time import sleep
from threading import Thread

import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import mysql.connector as sql
import random
import pandas as pd
import webbrowser
import datetime     
import pyjokes 
from tkinter import * 
import time 
import subprocess 
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser
from PIL import Image, ImageTk
from time import sleep
from threading import Thread
import pyttsx3


# In[ ]:


import subprocess
import wolframalpha
import pyttsx3
import random
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import json
import feedparser
import smtplib
import datetime 
import requests
from twilio.rest import Client
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen#<div class="open_grepper_editor" title="Edit & Save To Grepper"></div>


# In[ ]:


def callVoiceAssistant():
    
    voiceEngine = pyttsx3.init('sapi5')
    voices = voiceEngine.getProperty('voices')
    voiceEngine.setProperty('voice', voices[1].id)
    
#     def attachTOframe(text,bot=False):
#         if bot:
#             botchat = Label(chat_frame,text=text, bg="white", fg="black", justify=LEFT, wraplength=250, font=('Montserrat',12, 'bold'))
#             botchat.pack(anchor='w',ipadx=5,ipady=5,pady=5)
#         else:
#             userchat = Label(chat_frame, text=text, bg="black", fg='white', justify=RIGHT, wraplength=250, font=('Montserrat',12, 'bold'))
#             userchat.pack(anchor='e',ipadx=2,ipady=2,pady=5)

    def speak(text, display=False, icon=False):
        AITaskStatusLbl['text'] = 'Speaking...'
        if icon: Label(chat_frame, bg='white').pack(anchor='w',pady=0)
        #if display: attachTOframe(text, True)
        voiceEngine.say(text)
        voiceEngine.runAndWait()#<div class="open_grepper_editor" title="Edit & Save To Grepper"></div>

    def wish():
        print("Wishing.")
        time = int(datetime.datetime.now().hour)
        global uname,asname
        if time>= 0 and time<12:
            speak("Good Morning!")

        elif time<18:
            speak("Good Afternoon!")

        else:
            speak("Good Evening!")

        asname ="DIVA"
        speak("I am your Voice Assistant")
        speak(asname)
        print("I am your Voice Assistant,",asname)
    def getName():
        global uname
        speak("Can I please know your name?")
        uname = takeCommand()
        print("Name:",uname)
        speak("I am glad to know you!")
        #columns = shutil.get_terminal_size().columns
        speak("How can i Help you, ")
        speak(uname)

    def takeCommand(clearChat=True, iconDisplay=True):
        print('\nListening...')
        AITaskStatusLbl['text'] = 'Listening...'
        recog = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening to the user")
            recog.pause_threshold = 1
            userInput = recog.listen(source)

        try:
            print("Recognizing the command")
            AITaskStatusLbl['text'] = 'Processing...'
            command = recog.recognize_google(userInput, language ='en-in')
            print(f"Command is: {command}\n")
            if iconDisplay: Label(chat_frame, bg='white').pack(anchor='e',pady=0)
            #attachTOframe(command)

        except Exception as e:
            print(e)
            print("Unable to Recognize the voice.")
            return "None"

        return command#<div class="open_grepper_editor" title="Edit & Save To Grepper"></div>

    def sendEmail(to, content):
        print("Sending mail to ", to)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        #paste your email id and password in the respective places
        server.login('your email id', 'password') 
        server.sendmail('your email id', to, content)
        server.close()

    def getWeather(city_name):
        cityName=place.get() #getting input of name of the place from user
        baseUrl = "http://api.openweathermap.org/data/2.5/weather?" #base url from where we extract weather report
        url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + cityName  
        response = requests.get(url)
        x = response.json()

        #If there is no error, getting all the weather conditions
        if x["cod"] != "404":
            y = x["main"]
            temp = y["temp"]
            temp-=273 
            pressure = y["pressure"]
            humidity = y["humidity"]
            desc = x["weather"]
            description = z[0]["description"]
            info=(" Temperature= " +str(temp)+"°C"+"\n atmospheric pressure (hPa) ="+str(pressure) +"\n humidity = " +str(humidity)+"%" +"\n description = " +str(description))
            print(info)
            speak("Here is the weather report at")
            speak(city_name)
            speak(info)
        else:
            speak(" City Not Found ")

    def getNews():
        try:
            response = requests.get('https://www.bbc.com/news')

            b4soup = BeautifulSoup(response.text, 'html.parser')
            headLines = b4soup.find('body').find_all('h3')
            unwantedLines = ['BBC World News TV', 'BBC World Service Radio',
                        'News daily newsletter', 'Mobile app', 'Get in touch']

            for x in list(dict.fromkeys(headLines)):
                if x.text.strip() not in unwantedLines:
                    print(x.text.strip())
        except Exception as e:
            print(str(e))#<div class="open_grepper_editor" title="Edit & Save To Grepper"></div>

    if __name__ == '__main__':

        uname=''
        asname=''
        os.system('cls')
        wish()
        getName()
        print(uname)

        while True:

            command = takeCommand().lower()
            print(command)

            if "jarvis" in command:
                wish()

            elif 'how are you' in command:
                speak("I am fine, Thank you")
                speak("How are you, ")
                speak(uname)

            elif "good morning" in command or "good afternoon" in command or "good evening" in command:
                speak("A very" +command)
                speak("Thank you for wishing me! Hope you are doing well!")

            elif 'fine' in command or "good" in command:
                speak("It's good to know that your fine")

            elif "who are you" in command:
                speak("I am your virtual assistant.")

            elif "change my name to" in command:
                speak("What would you like me to call you, Sir or Madam ")
                uname = takeCommand()
                speak('Hello again,')
                speak(uname)

            elif "change name" in command:
                speak("What would you like to call me, Sir or Madam ")
                assname = takeCommand()
                speak("Thank you for naming me!")

            elif "what's your name" in command:
                speak("People call me")
                speak(assname)

            elif 'time' in command:
                strTime = datetime.datetime.now()
                curTime=str(strTime.hour)+"hours"+str(strTime.minute)+"minutes"+str(strTime.second)+"seconds"
                speak(uname)
                speak(f" the time is {curTime}")
                print(curTime)

            elif 'wikipedia' in command:
                speak('Searching Wikipedia')
                command = command.replace("wikipedia", "")
                results = wikipedia.summary(command, sentences = 3)
                speak("These are the results from Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in command:
                speak("Here you go, the Youtube is opening\n")
                webbrowser.open("youtube.com")

            elif 'open google' in command:
                speak("Opening Google\n")
                webbrowser.open("google.com")

            elif 'play music' in command or "play song" in command:
                speak("Enjoy the music!")
                music_dir = "C:\\Users\\Gayathri\\Music"
                songs = os.listdir(music_dir)
                print(songs)
                random = os.startfile(os.path.join(music_dir, songs[1]))

            elif 'joke' in command:
                speak(pyjokes.get_joke())

            elif 'mail' in command:
                try:
                    speak("Whom should I send the mail")
                    to = input()
                    speak("What is the body?")
                    content = takeCommand()
                    sendEmail(to, content)
                    speak("Email has been sent successfully !")
                except Exception as e:
                    print(e)
                    speak("I am sorry, not able to send this email")

            elif 'exit' in command:
                speak("Thanks for giving me your time")
                
                exit()

            elif "will you be my gf" in command or "will you be my bf" in command:
                speak("I'm not sure about that, may be you should give me some time")

            elif "i love you" in command:
                speak("Thank you! But, It's a pleasure to hear it from you.")

            elif "weather" in command:
                speak(" Please tell your city name ")
                print("City name : ")
                cityName = takeCommand()
                getWeather(cityName)

            elif "what is" in command or "who is" in command:

                client = wolframalpha.Client("API_ID")
                res = client.query(command)

                try:
                    print (next(res.results).text)
                    speak (next(res.results).text)
                except StopIteration:
                    print ("No results")

            elif 'search' in command:
                command = command.replace("search", "")
                webbrowser.open(command)

            elif 'news' in command:
                getNews()

            elif "don't listen" in command or "stop listening" in command:
                speak("for how much time you want to stop me from listening commands")
                a = int(takeCommand())
                time.sleep(a)
                print(a)

            elif "camera" in command or "take a photo" in command:
                ec.capture(0, "Jarvis Camera ", "img.jpg")

            elif 'shutdown system' in command:
                    speak("Hold On a Sec ! Your system is on its way to shut down")
                    subprocess.call('shutdown / p /f')

            elif "restart" in command:
                subprocess.call(["shutdown", "/r"])

            elif "sleep" in command:
                speak("Setting in sleep mode")
                subprocess.call("shutdown / h")

            elif "write a note" in command:
                speak("What should i write, sir")
                note = takeCommand()
                file = open('jarvis.txt', 'w')
                speak("Sir, Should i include date and time")
                snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)
            else:
                speak("Sorry, I am not able to understand you")#<div class="open_grepper_editor" title="Edit & Save To Grepper"></div>

from tkinter import *
import tkinter as tk
wn = tk.Tk() 
wn.title("DIVA Voice Assistant")
wn.geometry('700x300')
wn.config(bg='LightBlue1')

Label(wn, text='DIVA', bg='LightBlue1',
      fg='black', font=('Courier', 15)).place(x=50, y=10)

chat_frame = Frame(wn, width=380,height=551,bg='white')
chat_frame.pack(padx=10)

AITaskStatusLbl = Label(wn, text='    Offline', fg='black', font=('montserrat', 16))
AITaskStatusLbl.place(x=140,y=32)
#Label(wn, msg1)

#Button to convert PDF to Audio form
Button(wn, text="Start", bg='gray',font=('Courier', 15),
       command= callVoiceAssistant).place(x=290, y=100)

#Runs the window till it is closed
wn.mainloop()
                
#callVoiceAssistant()


# In[ ]:




