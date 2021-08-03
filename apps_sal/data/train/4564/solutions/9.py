from functools import reduce


def create_phone_number(n):
    return reduce(lambda a, c: a.replace('x', c, 1), list(map(str, n)), '(xxx) xxx-xxxx')
