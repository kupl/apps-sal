import re


def time_correct(t):
    if not t:
        return t

    if not re.match("\d\d:\d\d:\d\d$", t):
        return None

    hours, minutes, seconds = [int(x) for x in t.split(':')]

    if seconds >= 60:
        minutes += 1
        seconds -= 60
    if minutes >= 60:
        hours += 1
        minutes -= 60
    if hours >= 24:
        hours = hours % 24

    return "{0:0>2}:{1:0>2}:{2:0>2}".format(hours, minutes, seconds)
