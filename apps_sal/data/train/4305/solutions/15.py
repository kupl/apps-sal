def order_weight(s): return ' '.join(sorted(s.split(), key=lambda s: (sum(map(int, s)), s)))
