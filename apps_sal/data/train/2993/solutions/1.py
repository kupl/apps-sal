from itertools import zip_longest
def poly_add(p1, p2):
    return [x+y for x, y in zip_longest(p1, p2, fillvalue=0)]
