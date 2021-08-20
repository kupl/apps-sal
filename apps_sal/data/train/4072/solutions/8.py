def permutation_position(perm):
    return 1 + sum(((ord(c) - 97) * 26 ** i for (i, c) in enumerate(perm[::-1])))
