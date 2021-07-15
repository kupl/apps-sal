import math

def round_to_next5(n):
    res = 5 * math.floor(n/5)
    if n < 0 and n != res:
        return res + 5
    elif n < 0 and n == res:
        return res
    return math.ceil(n/5) * 5
