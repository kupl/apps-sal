import math
def round_it(n):
    s = str(n).split('.')
    print(s[0], s[1])
    return math.floor(n) if len(s[0]) > len(s[1]) else math.ceil(n) if len(s[0]) < len(s[1]) else round(n)
