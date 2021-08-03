import math


def find_difference(a, b):
    def prod(arr):
        proc = 1
        for i in arr:
            proc *= i
        return proc

    return abs(prod(a) - prod(b))
