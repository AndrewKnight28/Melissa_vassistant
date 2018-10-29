import os
import unicodedata
import speech_recognition as sr
from ptts import ptts

def recorder():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        sound = r.recognize_google(audio).lower().replace("'","")   #to change language add (audio, language = "en-US") 
        speech_text = sound.encode('ascii', 'ignore')   #deletes all non ascii chars
        print("Melissa thinks you said '" + speech_text + "'")
        return speech_text
    except sr.UnknownValueError:
        print("Melissa did not understand.")
        ptts('I dont understand, Can you repeat please?')
        recorder()
    except sr.RequestError as e:
        print("Could not request results from Melissa;{0}".format(e))
        ptts('I dont understand, Can you repeat please?')
        recorder()
