import re
def time_correct(t):
    if t and re.match(r"\d\d:\d\d:\d\d", t):
        h,m,s = t.split(":")
        seconds = int(s)
        minutes = int(m) + seconds // 60
        hours = int(h) + minutes // 60
        return "%02d:%02d:%02d" % (hours % 24, minutes % 60, seconds % 60)
    return None if t != '' else ''

