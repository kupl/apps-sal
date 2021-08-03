from functools import reduce


def greatest_product(a):
    return max([reduce(lambda a, b: a * b, map(int, a[i: i + 5])) for i in range(0, len(a) - 4)])
