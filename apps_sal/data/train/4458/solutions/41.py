import re


def time_correct(t):
    if t is None or not t:
        return t
    if not re.match(r'^(\d\d:){2}\d\d$', t):
        return None
    seconds = sum(int(c, 10) * 60 ** (2 - i) for i, c in enumerate(t.split(':')))
    return '{:02d}:{:02d}:{:02d}'.format(seconds // 3600 % 24, seconds // 60 % 60, seconds % 60)
