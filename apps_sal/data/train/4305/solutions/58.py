def order_weight(string):
    return ' '.join(sorted(string.split(), key=lambda x: (sum(int(i) for i in x), x)))
