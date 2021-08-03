import itertools


def permutations(s):
    return list(set([''.join(x) for x in itertools.permutations(list(s))]))
