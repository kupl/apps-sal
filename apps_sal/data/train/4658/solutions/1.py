def max_product(lst, n):
    from functools import reduce
    return reduce(lambda x,y: x*y, sorted(lst, reverse=True)[:n])
