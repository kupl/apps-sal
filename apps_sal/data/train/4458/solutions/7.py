import re

def time_correct(t):
    if not t:
        return t
    if re.match(r'\d\d:\d\d:\d\d$', t):
        hours, minutes, seconds = list(map(int, t.split(':')))
        d_minutes, seconds = divmod(seconds, 60)
        d_hours, minutes = divmod(minutes + d_minutes, 60)
        hours = (hours + d_hours) % 24
        return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

