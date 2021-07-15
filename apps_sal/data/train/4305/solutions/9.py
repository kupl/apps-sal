def order_weight(strng):
    return ' '.join(sorted(sorted(strng.split()), key=lambda w: sum([int(c) for c in w])))
