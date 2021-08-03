import math


def square_sum(numbers):
    result = 0
    for c in numbers:
        result += math.pow(c, 2)
    return result
