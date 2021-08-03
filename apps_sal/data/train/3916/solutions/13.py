import numpy


def mean_vs_median(numbers):
    mean = numpy.mean(numbers)
    median = numpy.median(numbers)
    if mean == median:
        return 'same'
    return 'mean' if mean > median else 'median'
