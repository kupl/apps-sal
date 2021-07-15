from functools import reduce

def max_product(l, k):
    return reduce(lambda res, x:res * x,sorted(l)[-k:])
