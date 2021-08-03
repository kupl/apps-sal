import numpy


def is_orthogonal(u, v):
    c = numpy.dot(u, v)
    if c:
        return False
    return True
