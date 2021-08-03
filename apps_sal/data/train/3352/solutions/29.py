from math import floor, log10


def find_longest(arr):
    def digits(a): return floor(log10(a))
    return max(arr, key=digits)
