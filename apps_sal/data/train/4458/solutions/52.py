import re

def time_correct(t):
    if not t:
        return t
    
    if not re.match("\d\d:\d\d:\d\d$", t):
        return None
    
    hours,minutes,seconds = t.split(':')
    hours,minutes,seconds = int(hours), int(minutes), int(seconds)
    
    while seconds > 59:
        minutes+=1
        seconds-=60

    
    while minutes > 59:
        hours+=1
        minutes-=60

    
    while hours >= 24:
        hours-=24
    
    return '{:02}:{:02}:{:02}'.format(hours,minutes,seconds)
    

