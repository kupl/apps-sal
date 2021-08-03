import math


def round_it(n):
    s = str(n).split('.')
    l = len(s[0])
    r = len(s[1])
    return math.ceil(n) if l < r else math.floor(n) if l > r else round(n)
