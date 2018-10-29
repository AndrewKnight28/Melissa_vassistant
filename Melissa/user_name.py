import re
import yaml
import sys
import ruamel.yaml

yaml = ruamel.yaml.YAML()

from GreyMatter.SenseCells.ptts import ptts
from GreyMatter.SenseCells.recognizer import recorder

def name_change(speech_text):
    new_name = speech_text.split()
    new_name.remove('call')
    new_name.remove('me')
    nombre = ' '.join(new_name)
    #changes yaml file
    with open('profile.yaml') as profile:
        profile_data = yaml.load(profile)
    profile_data['name'] = nombre
    name = profile_data['name']
    with open('profile.yaml', 'w') as profile:
        yaml.dump(profile_data, profile)

    return name

#must add -t arg to run on text_mode
def is_correct(speech_text, name):
    ptts('Is ' + name + ' correct?')
    print('Is ' + name +' correct?')
    speech_text = recorder()

    if (speech_text == 'no') or (speech_text == 'No'):
        return False
    else:
        #if name is correct then program must restart
        quit()        
        return True
