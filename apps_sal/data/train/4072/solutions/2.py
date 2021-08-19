def permutation_position(perm):
    return sum(((ord(c) - 97) * 26 ** i for (i, c) in enumerate(reversed(perm)))) + 1
