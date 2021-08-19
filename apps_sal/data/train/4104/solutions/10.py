import itertools


def max_tri_sum(numbers):
    return max((sum(i) for i in itertools.combinations(set(numbers), 3)))
