from array import *


def between(a, b):
    arr = array('i', range(a, b + 1))
    return [a for a in arr]
