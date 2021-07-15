from functools import reduce

def find_difference(a, b):
    volume = lambda a,b:a*b
    return abs(reduce(volume, a) - reduce(volume, b))
