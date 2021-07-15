from functools import reduce 

def max_product(l, n):
    return reduce(lambda x,y: x*y,sorted(l)[-n:])

