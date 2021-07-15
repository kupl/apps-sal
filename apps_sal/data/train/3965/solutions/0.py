from math import log

def powerof4(n):
    if type(n) in (float, int) and n > 0:
        return log(n,4).is_integer()
    return False
