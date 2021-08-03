from itertools import starmap
from operator import sub
from math import hypot


def length_of_line(array):
    return '{:.2f}'.format(hypot(*starmap(sub, zip(*array))))
