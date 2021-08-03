import re


def time_correct(t):
    if not t:
        return t
    if not re.match(r"(\d{2}:){2}\d{2}", t):
        return None
    h, m, s = map(int, t.split(":"))
    t = h * 3600 + m * 60 + s
    h = t // 3600 % 24
    t %= 3600
    m = t // 60
    t %= 60
    return f"{h:0>2}:{m:0>2}:{t:0>2}"
