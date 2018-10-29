import re
import wikipedia

from SenseCells.ptts import ptts

def define(speech_text):
    words_of_message = speech_text.split()
    words_of_message.remove('define')
    cleaned = ' '.join(words_of_message)
    try:
        wiki_data = wikipedia.summary(cleaned, sentences=2)
        regEx = re.compile(r'([^\(]*)\([^\)]*\) *(.*)')
        m = regEx.match(wiki_data)
        while m:
            wiki_data = m.group(1) + m.group(2)
            m = regEx.match(wiki_data)

        wiki_data = wiki_data.replace("'", "")
        ptts(wiki_data)
    except wikipedia.exceptions.DisambiguationError as e:
        ptts('Could you be more specific? You can choose one of the following.')
        #shows all the options
        print("Could you be more specific? You can choose one of the following.; {0}".format(e))
