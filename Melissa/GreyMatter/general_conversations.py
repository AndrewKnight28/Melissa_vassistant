from SenseCells.ptts import ptts
import os
import random

def who_are_you():
    ptts('My name is Melissa. Your lovely assistant')

def tell_joke():
    jokes = ['Joke', 'Once there was an ulgy barnacle. He was so ugly, that everyone died. The end.'] #LOL patrick
    ptts(random.choice(jokes))

def who_am_i(name):
    ptts('Your name is ' + name + ', you are the current user.')

def where_born(city_name):
    ptts('You are from' + city_name)
#could add a default mp3 file for optimization
def how_are_you():
    ptts('I am fine. Thanks for asking.')

def undefined():
    ptts('Sorry i did not understant.')
