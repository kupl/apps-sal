def order_weight(strng):
    key = lambda s: (sum((int(d) for d in s)), s)
    return ' '.join(sorted(strng.split(), key=key))


