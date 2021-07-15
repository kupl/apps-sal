def order_weight(string):
    return " ".join(sorted(string.split(), key=lambda s: (sum(int(d) for d in list(s)), s)))
