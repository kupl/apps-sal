def greek_comparator(lhs, rhs):
    if lhs == rhs:
        return 0
    if greek_alphabet.index(lhs) < greek_alphabet.index(rhs):
        return -1
    if greek_alphabet.index(lhs) > greek_alphabet.index(rhs):
        return 1
