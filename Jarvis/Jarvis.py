import pyttsx3  #pip install pyttsx3
import speech_recognition as sr  #pip install speechRecognition
import datetime
import wikipedia   #pip install wikipedia
import webbrowser
import os
import smtplib

print("Initializing Jarvis")
MASTER = "Shivam"

engine = pyttsx3.init('Sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#speak function will pronounce the string which is passed to it 
def speak(text):
    engine.say(text)
    engine.runAndWait()

#This function will wish you as per current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    #print(hour)
    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)
    elif hour>=12 and hour <18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
    speak("I am Jarvis.  How may I help you?")
    
#This function take command from Microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please")
        query = None
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','password')
    server.sendmail("shivamgupta17600@gmail.com", to, content)
    server.close()

                 
#Main Program
def main():

    #speak("Initializing Jarvis...")
    wishme()
    query = takeCommand()

        #Logic for executing query as per task
    if 'wikipedia' in query.lower():
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences =2)
            print(results) 
            speak(results)

    elif 'open youtube' in query.lower:
            #webbrowser.open("Youtube.com")
            url = "youtube.com"
            chrome_path = 'C:/Program Files (x86)/Google\Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url) 

    elif 'open google' in query.lower:
            #webbrowser.open("Youtube.com")
            url = "google.com"
            chrome_path = 'C:/Program Files (x86)/Google\Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url) 

    elif 'open stackoverflow' in query.lower:
            #webbrowser.open("Youtube.com")
            url = "stackoverflow.com"
            chrome_path = 'C:/Program Files (x86)/Google\Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

    elif 'open reddit' in query.lower:
            #webbrowser.open("Youtube.com")
            url = "reddit.com"
            chrome_path = 'C:/Program Files (x86)/Google\Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
            songs_dir = ""
            songs = os.listdir("")
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[0]))
            
    elif 'play movie' in query.lower():
            movie_dir = ""
            movie = os.listdir("")
            print(movie)
            os.startfile(os.path.join(movie_dir, movie[0]))
            
    elif 'the time' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{Master} the time is{strTime}")

    elif 'open code' in query.lower():
            codePath =""
            os.startfile(codepath)

    elif 'email to shivam' in query.lower():
        try:
            speak("What should i send")
            content = takeCommand()
            to = "shivamgupta17600@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent Successfully")

        except Exception as e:
            print(e)
            speak("Soory i am not able to send e-mail")

    
    elif 'youtube' in query:
            #webbrowser.open("Youtube.com")
        speak('Opening youtube...')  
        query = query.replace("youtube", "")
        results = youtube.summary(query)
        url = "youtube.com"
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url) 
    






















    






    
