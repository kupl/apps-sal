from functools import reduce


def find_difference(a, b):

    def prod(x, y):
        return x * y
    return abs(reduce(prod, a) - reduce(prod, b))
