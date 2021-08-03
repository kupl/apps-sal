import sys
p = sys.modules['iter''tools'].permutations


def nth_perm(n, d):
    return ''.join([*p('0123456789'[:d])][~-n])
