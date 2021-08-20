def greek_comparator(lhs, rhs):
    if lhs == rhs:
        return 0
    (l, r) = (0, 0)
    for (i, a) in enumerate(greek_alphabet):
        if lhs == a:
            l = i
        if rhs == a:
            r = i
    return -1 if l < r else 1
