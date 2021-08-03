import numpy


def billboard(name, price=30):
    return numpy.prod([len(name), price])
