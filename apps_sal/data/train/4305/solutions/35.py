def order_weight(strng):
    return ' '.join(sorted(strng.split(), key=lambda x: (sum((int(i) for i in str(x))), x)))
