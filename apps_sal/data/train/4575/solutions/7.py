from itertools import chain, count


def smallest_integer(matrix):
    xs = set(chain.from_iterable(matrix))
    return next((i for i in count(0) if i not in xs))
