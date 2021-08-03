from itertools import compress, product


def powerset(a):
    return [list(compress(a, p)) for p in product((0, 1), repeat=len(a))]
