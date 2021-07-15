from math import log, ceil

def fold_to(d):
    return None if d < 0 else 0 if d < 0.0001 else ceil(log(d/0.0001, 2))
