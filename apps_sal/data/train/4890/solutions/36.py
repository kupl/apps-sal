import numpy


def find_difference(a, b):
    return abs(numpy.prod(b) - numpy.prod(a))
