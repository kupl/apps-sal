import sys


def max_tri_sum(numbers):
    numbers = sorted(list(set(numbers)))
    return sum(numbers[-3:])
