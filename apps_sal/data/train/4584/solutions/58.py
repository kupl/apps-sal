def invert(lst):
    return list((abs(el) if el < 0 else -el for el in lst))
