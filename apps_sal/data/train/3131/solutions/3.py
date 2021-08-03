from functools import reduce


def product(x):
    return reduce(lambda a, b: a * b, (int(d) for d in str(x)), 1)


def unique_digit_products(a):
    return len({product(x) for x in a})
