from functools import reduce
def max_product(lst, n): return reduce(lambda x, y: x * y, sorted(lst, reverse=True)[:n])
