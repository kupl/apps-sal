from functools import reduce


def digit_sum(n):
    return sum(int(i) for i in str(n))


def digit_product(n):
    return reduce(lambda a, b: a * int(b), str(n), 1)
    # return reduce(lambda a, b: a * b, map(int, str(n)), 1)


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y / gcd(x, y)


def parameter(n):
    return lcm(digit_sum(n), digit_product(n))
