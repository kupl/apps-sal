from functools import reduce
def max_product(ls, k):
    return reduce(lambda a,c: a*c, sorted(ls ,reverse=True)[:k], 1)
