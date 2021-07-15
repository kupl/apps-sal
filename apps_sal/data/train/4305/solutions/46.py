def order_weight(string):
    return ' '.join(sorted(string.split(), key= lambda s: (sum(int(i) for i in s), s)))
