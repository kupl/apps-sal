import itertools


def permutations(string):
    return set((''.join(x) for x in itertools.permutations(string, r=len(string))))
