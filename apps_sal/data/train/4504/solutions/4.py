from functools import reduce


def share_price(invested, changes):
    r = reduce(lambda acc, x: acc + x * acc * 0.01, changes, invested)
    return '{:.2f}'.format(r)
