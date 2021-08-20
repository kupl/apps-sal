import math


def index(array, n):
    if len(array) == 0:
        return -1
    for i in array:
        if n > len(array) - 1:
            return -1
        if i is array[n]:
            return math.pow(i, n)
