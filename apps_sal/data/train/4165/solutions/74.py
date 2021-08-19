from functools import reduce


def uni_total(s):
    return reduce(lambda a, b: a + ord(b), s, 0)
