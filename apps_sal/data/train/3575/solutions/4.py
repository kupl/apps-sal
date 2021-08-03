def powerset(a): return [[n for i, n in enumerate(a)if b >> len(a) - i - 1 & 1]for b in range(1 << len(a))]
