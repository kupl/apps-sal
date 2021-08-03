def nth_smallest(a, n): return None if len(set(a)) < n else list(sorted(set(a)))[n - 1]
