def order_weight(strng):
    return ' '.join(sorted(strng.split(), key=lambda n: (sum(map(int, n)), n)))
