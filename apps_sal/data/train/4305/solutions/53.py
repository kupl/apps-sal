def order_weight(s):
    return ' '.join(sorted(s.split(), key=lambda e: [sum(map(int, e)), e]))
