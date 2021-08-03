import math


def even_digit_squares(a, b):
    evens = ('2', '4', '6', '8', '0')
    start = math.ceil(math.sqrt(a))
    stop = math.ceil(math.sqrt(b + 1))
    return [n * n for n in range(start, stop) if all(i in evens for i in str(n * n))]
