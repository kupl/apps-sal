from itertools import repeat


def square_sum(numbers):
    return sum(map(pow, numbers, repeat(2)))
