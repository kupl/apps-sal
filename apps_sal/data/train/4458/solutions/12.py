import re

def time_correct(t):
    if not t: return t
    
    m = re.findall(r'^(\d{2}):(\d{2}):(\d{2})$', t)
    if m:
        h, m, s = map(int, m[0])
        if s >= 60:
            m += 1
            s %= 60 
        if m >= 60:
            h += 1
            m %= 60
        h %= 24
        return f"{h:02}:{m:02}:{s:02}"
