def order_weight(strng):
    return ' '.join(sorted(sorted([x for x in strng.split()]), key=lambda y: sum(map(int, y))))
