
from GreyMatter import general_conversations, tell_time, weather_t, define_subject, sleep, repeat
from user_name import name_change, is_correct


def brain(name, city_name, speech_text):
    def check_message(check):
        words_of_message = speech_text.split()
        if set(check).issubset(set(words_of_message)):
            return True
        else:
            return False

    #must find a way to optimaze the menu
    if check_message(['who','are', 'you']) or check_message(['your', 'name']):
        general_conversations.who_are_you()
    elif check_message(['call','me']):
        name = name_change(speech_text)
        while(is_correct(speech_text, name) == False):
                name = name_change(speech_text)    
    elif check_message(['where', 'born']):
        general_conversations.where_born(city_name)
    elif check_message(['how', 'are', 'you']):
        general_conversations.how_are_you()
    elif check_message(['thank', 'you']):
        sleep.go_to_sleep(name)
    elif check_message(['time']):
        tell_time.what_is_time()
    elif check_message(['tell', 'joke']):
        general_conversations.tell_joke()
    elif check_message(['who', 'am', 'i']) or check_message(['my', 'name']):
        general_conversations.who_am_i(name)
    elif check_message(['repeat']):
        repeat.repeat_after(speech_text)
    elif check_message(['how', 'weather']) or check_message(['hows', 'weather']):
        weather_t.weather(city_name)
    elif check_message(['define']):
        define_subject.define(speech_text)
    else:
        general_conversations.undefined()
