from functools import reduce

vol = lambda l: reduce(lambda x,y:x * y, l)

def find_difference(a, b):
    return abs(vol(b)-vol(a))
