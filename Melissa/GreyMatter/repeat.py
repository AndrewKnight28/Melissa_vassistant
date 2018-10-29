import re

from SenseCells.ptts import ptts

def repeat_after(speech_text):
    mensaje = speech_text.split()
    mensaje.remove('repeat')
    limpio = ' '.join(mensaje)
    ptts(limpio)
