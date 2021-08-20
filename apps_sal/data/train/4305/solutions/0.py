def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum((int(c) for c in x))))
