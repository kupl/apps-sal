def greek_comparator(lhs, rhs):
    # the tuple greek_alphabet is defined in the nonlocal namespace
    if lhs == rhs:
        return 0
    for pair in list(enumerate(greek_alphabet)):
        if pair[1] == lhs:
            valL = pair[0]
        if pair[1] == rhs:
            valR = pair[0]
    return -1 if valL < valR else 1
