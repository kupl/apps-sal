from functools import reduce


def sum_str(*args):
    return str(reduce(lambda x, y: int(x or 0) + int(y or 0), args))
