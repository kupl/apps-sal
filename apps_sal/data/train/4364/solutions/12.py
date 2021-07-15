import math

def odd_or_even(arr):
    i = sum(arr)
    if (i % 2) == 0:
        return "even"
    else:
        return "odd"
