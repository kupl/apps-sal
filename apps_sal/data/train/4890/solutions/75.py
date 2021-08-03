from functools import reduce


def find_difference(a, b):
    a_vol = reduce(lambda x, y: x * y, a)
    b_vol = reduce(lambda x, y: x * y, b)

    return max(a_vol, b_vol) - min(a_vol, b_vol)
