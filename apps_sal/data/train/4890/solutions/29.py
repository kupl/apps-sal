from functools import reduce

def find_difference(a, b):
    prod = lambda x, y: x * y
    return abs(reduce(prod, a) - reduce(prod, b))
