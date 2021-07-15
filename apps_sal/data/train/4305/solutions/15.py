order_weight=lambda s:' '.join(sorted(s.split(),key=lambda s:(sum(map(int,s)),s)))
