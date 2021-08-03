def order_weight(s): return ' '.join(sorted(sorted(s.split(' ')), key=lambda i: sum(map(int, i))))
