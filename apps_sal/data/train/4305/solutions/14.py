def order_weight(s):
    return ' '.join(sorted(sorted(s.split()), key=lambda x: sum(int(i) for i in x)))
