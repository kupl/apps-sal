def order_weight(string):
    return ' '.join(sorted(string.split(), key=lambda x: (sum([int(s) for s in x]), x), reverse=False))
