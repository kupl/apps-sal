from itertools import chain


def pairwise(a):
    return list(zip(a, a[1:]))


def transpose(a):
    return list(zip(*a))


def different_squares(matrix):
    if 1 in (len(matrix), len(matrix[0])):
        return 0
    all_squares = chain.from_iterable(map(pairwise, map(transpose, pairwise(matrix))))
    unique_squares = set(all_squares)
    return len(unique_squares)
