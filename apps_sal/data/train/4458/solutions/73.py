import re


def time_correct(t):
    if t == '':
        return ''
    if not t or not re.search("[0-9][0-9]:[0-9][0-9]:[0-9][0-9]", t):
        return None
    t = t.split(':')
    hour, min, sec = [int(x) for x in t]
    if sec > 59:
        min += (sec / 60)
        sec %= 60
    if min > 59:
        hour += (min / 60)
        min %= 60
    if hour > 23:
        hour %= 24
    return "%02d:%02d:%02d" % (hour, min, sec)
