def order_weight(string):
    weights = string.split()
    return ' '.join(sorted(weights, key=lambda w: (sum(int(n) for n in w), w)))
