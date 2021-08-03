def choose_best_sum(t, k, l): return max((d for d in map(sum, __import__('itertools').combinations(l, r=k))if d <= t), default=None)
