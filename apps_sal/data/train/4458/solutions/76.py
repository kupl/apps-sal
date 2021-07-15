import re

def time_correct(t):
    if t == None or t == '':
        return t
    t_pattern = re.compile(r'\d\d:\d\d:\d\d')
    if t_pattern.search(t) == None:
        return None
    hours, minutes, seconds = [int(x) for x in t.split(':')]
    if seconds > 59:
        seconds = seconds - 60
        minutes = minutes + 1
    if minutes > 59:
        minutes = minutes - 60
        hours = hours + 1
    if hours == 24:
        hours = 0
    if hours > 24:
        hours = hours%24
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)


    
        

