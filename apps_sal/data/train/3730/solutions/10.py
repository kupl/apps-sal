from itertools import cycle


def capitalize(s):
    func = cycle((str.upper, str.lower))
    result = ''.join((next(func)(a) for a in s))
    return [result, result.swapcase()]
