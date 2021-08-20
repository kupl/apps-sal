def order_weight(s):
    return ' '.join(sorted(s.split(), key=lambda x: (sum((int(y) for y in x)), x)))
