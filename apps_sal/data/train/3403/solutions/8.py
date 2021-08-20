import numpy


def reorder(a, b):
    first = numpy.roll(numpy.array([i for i in range(0, int(a / 2))]), b)
    second = numpy.roll(numpy.array([i for i in range(int(a / 2), a)]), b)
    result = [[i for i in first], [j for j in second]]
    return result
