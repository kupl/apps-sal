import re


def time_correct(t):
    if not t:
        return t
    if not bool(re.match(r"\d{2}:\d{2}:\d{2}$", t)):
        return None
    h, m, s = map(int, t.split(":"))
    sec = h * 3600 + m * 60 + s
    sec %= (3600 * 24)
    return "{:02}:{:02}:{:02}".format(sec // 3600, (sec % 3600) // 60, sec % 60)
