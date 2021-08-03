def reorder(a, b):
    import numpy
    return [list(numpy.roll(numpy.split(numpy.arange(a), 2)[0], b)), list(numpy.roll(numpy.split(numpy.arange(a), 2)[1], b))]
