order_weight = lambda s: ' '.join(sorted(sorted(s.split()), key=lambda w: sum(map(int, w))))
