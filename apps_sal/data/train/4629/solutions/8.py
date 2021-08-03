from functools import cmp_to_key


def cmp_func(a, b):
    ab, ba = (a + b), (b + a)
    return (ab > ba) - (ab < ba)


def penalty(l):
    return ''.join(sorted(l, key=cmp_to_key(cmp_func)))
