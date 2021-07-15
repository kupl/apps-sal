def order_weight(s):
    return ' '.join(sorted(s.split(), key=lambda x: (sum(map(int, x)), x)))
