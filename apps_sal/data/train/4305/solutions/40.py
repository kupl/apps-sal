def order_weight(strng):
    return ' '.join(sorted(strng.split(), key=lambda w: (sum(map(int, w)), w)))
