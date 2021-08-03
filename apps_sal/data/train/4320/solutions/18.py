def greek_comparator(lhs, rhs):
    if lhs == rhs:
        return 0
    a = [greek_alphabet.index(x) for x in [lhs, rhs]]
    if a[0] > a[1]:
        return 1
    else:
        return -1
