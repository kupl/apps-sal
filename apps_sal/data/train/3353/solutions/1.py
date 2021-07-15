from itertools import zip_longest

def poly_subtract(a, b):
    return [x - y for x, y in zip_longest(a, b, fillvalue=0)]
