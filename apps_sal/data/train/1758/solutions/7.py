import itertools


def permutations(s):
    return list(set((''.join(p) for p in itertools.permutations(s))))
