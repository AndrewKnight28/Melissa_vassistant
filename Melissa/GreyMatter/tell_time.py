from datetime import datetime
from SenseCells.ptts import ptts

def what_is_time():
    ptts("Its" + datetime.strftime(datetime.now(), '%H:%M:%S'))
