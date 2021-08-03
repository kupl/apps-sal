from bisect import bisect_left, bisect

ss = set('13579')
ns = [i ** 3 for i in range(1, int((10 ** 17) ** (1 / 3)) + 3, 2) if set(str(i ** 3)) <= ss]
ns = [-n for n in ns[::-1]] + ns


def odd_dig_cubic(a, b):
    return ns[bisect_left(ns, a):bisect(ns, b)]
