from functools import reduce


def permutation_position(perm):
    return reduce(lambda t, c: t * 26 + ord(c) - 97, perm, 0) + 1
