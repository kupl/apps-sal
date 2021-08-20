def permutation_position(perm):
    return sum(('abcdefghijklmnopqrstuvwxyz'.index(x) * 26 ** i for (i, x) in enumerate(perm[::-1]))) + 1
