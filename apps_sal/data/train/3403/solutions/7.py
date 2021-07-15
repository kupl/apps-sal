import numpy
def reorder(a, b):
    result = [list(numpy.roll([i for i in range(0, a//2)], b)), list(numpy.roll([i for i in range(a//2, a)], b))]
    return result
