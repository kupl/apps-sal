from math import floor, log10

def find_longest(arr):
    digits = lambda a: floor(log10(a))
    return max(arr, key=digits)
