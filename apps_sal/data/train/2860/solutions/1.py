from itertools import zip_longest


def isomorph(a, b):
    return len(set(a)) == len(set(b)) == len(set(zip_longest(a, b)))
