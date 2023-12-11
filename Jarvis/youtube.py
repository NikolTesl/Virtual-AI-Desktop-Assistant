import speech_recognition as spr
import webbrowser as wb
import pafy
import vlc
import urllib.request
from bs4 import BeautifulSoup
import time

linklist = []

recog1 = spr.Recognizer()
recog2 = spr.Recognizer()

mc = spr.Microphone(device_index=0)

with mc as source:
    print("Search Youtube video to play")
    print("----------")
    print("Speak")
    audio = recog1.listen(source)

if 'search' in recog1.recognize_google(audio):
    recog1 = spr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with mc as source:
        print('Searching for video(s)......')
        audio = recog2.listen(source)

        try:
            get_keyword = recog1.recognize_google(audio)
            print(get_keyword)
            wb.get().open_new(url+get_keyword)
            response = urllib.request.urlopen(url+get_keyword)
            html = response.read()
            soup = BeautifulSoup(html,  'html.parser')
            for vid in soup.findAll(attes={'class' : 'yt-uix-tile-link'}):
                linklist.append('https://www.youtube.com' +vid['href'])
                videolink = pafy.new(linklist[1])
                bestlink = videolink.getbest()
                media = vlc.MediaPlayer(bestlink.url)
                media.play()
                time.sleep(10)
                media.stop()   

        except spr.UnknownValueError:
            print("Unable to understand the input")
        except spr.RequestError as e:
            print("Unable to provide Output".format(e))    
