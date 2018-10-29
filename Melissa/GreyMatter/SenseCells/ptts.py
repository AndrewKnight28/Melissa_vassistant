import os
from gtts import gTTS

def ptts(message):  #p stands for personal
            tts_engine = gTTS(message, lang = 'en-us')
            filename = "temp.mp3"
            tts_engine.save(filename)   #saves audio file
            os.system("mpg321 " + filename) # reads audio file
            os.remove(filename) #deletes audio file

#i haven't found a better way to make a tts. Using espeak is awful. Maybe with polly.