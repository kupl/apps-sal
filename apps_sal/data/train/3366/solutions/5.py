import sys
p = sys.modules['itertools'].permutations


def nth_perm(n, d):
    return ''.join([*p('0123456789'[:d])][~-n])
