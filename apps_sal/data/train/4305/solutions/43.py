def order_weight(strng):
    return ' '.join(sorted(strng.split(), key=lambda s: (sum(map(int, s)), s)))
