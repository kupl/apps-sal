def unique_in_order(l):
    return [z for (i, z) in enumerate(l) if i == 0 or l[i - 1] != z]
