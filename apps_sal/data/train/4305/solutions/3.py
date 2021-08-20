def order_weight(strng):
    return ' '.join(sorted(strng.split(), key=lambda x: (sum((int(d) for d in x)), x)))
