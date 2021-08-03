def alternate_sq_sum(arr):
    return sum(v * v if i & 1 else v for i, v in enumerate(arr))
