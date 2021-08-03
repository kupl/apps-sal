def or_arrays(a1, a2, d=0): return [(a1[i] if i < len(a1) else d) | (a2[i] if i < len(a2) else d) for i in range(max(len(a1), len(a2)))]
