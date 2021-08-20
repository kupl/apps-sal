from itertools import accumulate


def sum_triangular_numbers(_):
    return sum(accumulate(range(0, _ + 1)))
