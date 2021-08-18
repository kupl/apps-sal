def order_weight(strng):
    return ' '.join(sorted(strng.split(), key=lambda x: (sum(int(c) for c in x), x)))
