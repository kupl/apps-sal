def order_weight(strng):
    return ' '.join(sorted(sorted(strng.split()), key=lambda s: sum(map(int, list(s)))))
