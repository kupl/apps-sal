import operator

def invert(lst):
    return list(map(operator.neg, lst))
