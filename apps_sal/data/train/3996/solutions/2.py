def alternate_sq_sum(arr):
    return sum((n * (n if i % 2 else 1) for (i, n) in enumerate(arr)))
