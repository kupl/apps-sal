from functools import reduce


def max_product(lst, n):
    st = sorted(lst)
    lg = st[-n:]
    return reduce(lambda x, y: x * y, lg)
