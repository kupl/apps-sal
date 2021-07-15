def order_weight(strng):
    return ' '.join(sorted(sorted(strng.split()), key=lambda weight: sum(map(int, weight))))
