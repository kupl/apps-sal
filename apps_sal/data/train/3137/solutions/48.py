import math

def round_it(n):
    a = str(n).split('.')
    return math.ceil(n) if len(a[0]) < len(a[1]) else math.floor(n) if len(a[0]) > len(a[1]) else round(n)
