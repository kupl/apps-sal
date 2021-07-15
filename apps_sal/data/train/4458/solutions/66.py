import re
def time_correct(t):
    if t and re.search(r'\d{2}:\d{2}:\d{2}', t): 
        h, m, s = [int(s) for s in t.split(':')]
        m, s = m+(s//60), s%60
        h, m = h+(m//60), m%60
        h = h%24
        return f'{h:02}:{m:02}:{s:02}'
    else:
        return '' if t=='' else None
