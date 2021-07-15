def order_weight(strng):
    return ' '.join(sorted(sorted(strng.split()), key=lambda s: sum([int(x) for x in s])))
