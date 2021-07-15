import numpy

def product_array(numbers):
    p = numpy.prod(numbers)
    return [p / i for i in numbers]
