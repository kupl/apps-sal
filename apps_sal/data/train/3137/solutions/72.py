import math


def round_it(n):
    s = str(n)
    if not '.' in s:
        return 0
    vor = s.index('.')
    nach = len(s) - s.index('.') - 1
    if vor > nach:
        return math.floor(n)
    if vor < nach:
        return math.ceil(n)
    else:
        return round(n)
