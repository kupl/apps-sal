def order_weight(s):
    return ' '.join(sorted(sorted(s.split()), key=lambda w: sum(map(int, w))))
