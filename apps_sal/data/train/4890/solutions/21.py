from functools import reduce


def find_difference(a, b):

    def volume(a, b):
        return a * b
    return abs(reduce(volume, a) - reduce(volume, b))
