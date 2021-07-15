def permutation_position(perm):
    return sum((ord(c) - 0x61) * (26 ** i) for i, c in enumerate(reversed(perm))) + 1
