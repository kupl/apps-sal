def order_weight(strng):
    return ' '.join(sorted(strng.split(), key=lambda x: (sum(map(int, x)), str(x))))
