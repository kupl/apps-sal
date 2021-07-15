from math import ceil, log
def evaporator(c, e, t):
    return ceil(log(t/100, 1-(e/100)))
