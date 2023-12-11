from gTTS import gTTS

text2speech = gTTS(text="Hello Shivam",lang='en')
text2speech.save(sample.mp3)
