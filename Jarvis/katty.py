import pyttsx3  #pip install pyttsx3
import speech_recognition as sr  #pip install speechRecognition
import datetime
import wikipedia   #pip install wikipedia
import webbrowser
import os
import smtplib

print("Initializing katty")
MASTER = "Shivam"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)
    elif hour>=12 and hour <18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
    speak("I am katty.  How may I help you?")

#This function take command from Microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        speak("Say that again please")
        print("Say that again please")
        query = None
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sender e-mail','password')
    server.sendmail("receiver e-mail", to, content)
    server.close()

speak("Initializing katty.....")
wishMe()
query = takeCommand()

#Logic for executing query as per task

if 'wikipedia' in query.lower():
    speak('Searching wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences = 2)
    speak("According to wikipedia...")
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    #webbrowser.open("Youtube.com")
    url = "youtube.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url) 

elif 'open google' in query.lower():
    #webbrowser.open("google.com")
    url = "google.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

elif 'open instagram' in query.lower():
    #webbrowser.open("google.com")
    url = "instagram.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

elif 'open facebook' in query.lower():
    #webbrowser.open("google.com")
    url = "facebook.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

elif 'open whatsapp' in query.lower():
    #webbrowser.open("google.com")
    url = "web.whatsapp.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

elif 'open linkedin' in query.lower():
    #webbrowser.open("google.com")
    url = "linkedin.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

elif 'open reddit' in query.lower():
    #webbrowser.open("google.com")
    url = "reddit.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

elif 'open stackoverflow' in query.lower():
    #webbrowser.open("google.com")
    url = "stackoverflow.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

elif 'music' in query.lower():
    songs_dir = "C:\\Users\\shivam gupta\\Music\\Mysong"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))

elif 'movie' in query.lower():
    movie_dir = "C:\\Marvel"
    movie = os.listdir(movie_dir)
    print(movie)
    os.startfile(os.path.join(movie_dir, movie[4]))

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is{strTime}")
    print(strTime)

elif 'open map' in query.lower():
    #webbrowser.open("google map")
    url = "https://www.google.co.in/maps"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url) 

elif 'email to shivam' in query.lower():
    try:
        speak("What should i send")
        content = takeCommand()
        to = "receiver e-mail"
        sendEmail(to, content)
        speak("Your Email has been sent Successfully")
    except Exception as e:
        print(e)
        speak("Soory i am not able to send e-mail")
