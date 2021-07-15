def order_weight(strng):
    return ' '.join([a[1] for a in sorted([(sum(int(y) for y in x), x) for x in strng.split(' ')])])
