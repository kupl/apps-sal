def order_weight(strng):
    return ' '.join(sorted(sorted(strng.split()),key = lambda x: sum(int(y) for y in x)))

