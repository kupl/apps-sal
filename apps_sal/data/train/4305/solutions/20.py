def order_weight(s):
    func = lambda x: sum(map(int, x))
    return ' '.join(sorted(s.split(), key=lambda x: (func(x), x)))
