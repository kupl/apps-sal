def alternate_sq_sum(arr):
    return sum(n ** 2 if c % 2 == 1 else n for c, n in enumerate(arr))
