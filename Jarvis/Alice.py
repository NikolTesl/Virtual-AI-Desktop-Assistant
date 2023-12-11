import speech_recognition as sr
import webbrowser
import time
from playsound import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()
def record_audio(ask=False):     
    with sr.Microphone() as source:
        Alice('Say Something')
        if ask:
            Alice(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            Alice(voice_data)
        except sr.UnknownValueError:
            Alice('sorry ,I did not get you')
        except sr.RequestError:
            Alice('Sorry, can you please say again')
        return voice_data

def Alice(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.random(1, 100000000)
    audio_file = 'audio-' +str(r) +'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'What is your name' in voice_data:
        Alice('My name is Alice')
    if 'What time is it' in voice_data:
        Alice(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search?')
        url = 'https://gooogle.com/search?q=' +search
        webbrowser.get().open(url)
        Alice('Here is what you search for' +search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://gooogle.nl/maps/place/' +location  + '/&amp;'
        webbrowser.get().open(url)
        Alice('Here is the location of' +location)
    if 'exit' in voice_data:
        exit()

time.sleep(1)
Alice('How can i help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
        












