import math


def length_of_line(array):
    return '%.2f' % math.hypot(array[1][0] - array[0][0], array[1][1] - array[0][1])
