order_weight = lambda s: ' '.join(sorted(sorted(s.split(' ')), key=lambda i: sum(map(int, i))))
