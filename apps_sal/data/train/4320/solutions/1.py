def greek_comparator(lhs, rhs):
    return 0 if lhs == rhs else -1 if greek_alphabet.index(lhs) < greek_alphabet.index(rhs) else 1
