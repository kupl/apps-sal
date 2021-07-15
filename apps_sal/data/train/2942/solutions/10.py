from math import log,ceil
def fold_to(d):
    if d>=0: return d and max(0, ceil(log(10000*d, 2)))

