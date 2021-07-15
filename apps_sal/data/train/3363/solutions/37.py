from math import log, ceil
def evaporator(content, e, t):
    return ceil(log(t/100,1-e/100))
