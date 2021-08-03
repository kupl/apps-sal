def array_leaders(a): return [a[i] for i in range(len(a)) if a[i] > sum(a[i + 1:])]
