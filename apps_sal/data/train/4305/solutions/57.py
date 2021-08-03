def order_weight(string):
    return ' '.join(sorted(string.split(), key=lambda s: (sum(map(int, s)), s)))
