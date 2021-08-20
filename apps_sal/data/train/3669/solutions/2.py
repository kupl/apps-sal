import itertools


def sc_perm_comb(num):
    return sum([int(''.join(p)) for i in range(1, len(str(num)) + 1) for p in set(itertools.permutations(str(num), i)) if p[0] != '0'])
