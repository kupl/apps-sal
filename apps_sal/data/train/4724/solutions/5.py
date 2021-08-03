import re


def r(m):
    s = m.group()
    if len(s) > 2:
        s = s.capitalize()
    return s


def drop_cap(s):
    return re.sub('\w+', r, s)
