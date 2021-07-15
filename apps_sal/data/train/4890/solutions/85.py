import numpy

def find_difference(a, b):
    aa = numpy.prod(a)
    bb = numpy.prod(b)
    return aa - bb if aa > bb else bb - aa
