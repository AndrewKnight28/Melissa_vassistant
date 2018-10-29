import sys
import os
import yaml
import random

from brain import brain
from GreyMatter.SenseCells.recognizer import recorder
from GreyMatter.SenseCells.ptts import ptts

#tex_mode (must run with -t)
if(len(sys.argv)==2):
    ini = sys.argv[1]
else:
    ini = 'a'

profile = open('profile.yaml')
profile_data = yaml.load(profile)
profile.close()

name = profile_data['name']
city_name = profile_data['city_name']
#Greeting
ptts('Welcome' + name + '. How can i help you?')

def main(ini):
    #text_mode
    if(ini == '-t'):
        speech_text = input("Write an order")
    #voice_mode
    else:
        speech_text = recorder()
    brain(name, city_name, speech_text)

#we initite
main(ini)
#here we add the loop
while True:
    ptts("Do you need something else?")
    main(ini)


                                                                                            #made by A.