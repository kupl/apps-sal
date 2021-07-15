import numpy

def to_binary(n):
    return numpy.binary_repr(n) if n>=0 else numpy.binary_repr(n, width=32)
