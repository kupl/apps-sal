import math

def round_it(n):
    s = str(n).split('.')
    if len(s[0]) > len(s[1]):
        return math.floor(n)
    if len(s[0]) < len(s[1]):
        return math.ceil(n)
    return round(n)
