import math
import numpy


def get_average(marks):
    number = numpy.average(marks)
    return math.floor(number)
