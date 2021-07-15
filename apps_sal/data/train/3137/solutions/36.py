import math
def round_it(n):
    sl = (str(n)).split('.')
    l0 = len(sl[0])
    l1 = len(sl[1])
    if l0 < l1:
        return math.ceil(n)
    elif l0 > l1:
        return math.floor(n)
    else:
        return round(n)

