import numpy

def max_gap(numbers):
    return max(numpy.diff(sorted(numbers)))
