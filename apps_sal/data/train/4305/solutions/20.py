def order_weight(s):
    def func(x): return sum(map(int, x))
    return ' '.join(sorted(s.split(), key=lambda x: (func(x), x)))
