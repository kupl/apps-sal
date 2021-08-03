import numpy


def opposite(number):
    if number < 0:
        return abs(number)
    else:
        return numpy.negative(number)
