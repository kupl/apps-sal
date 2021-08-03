def alternate_sq_sum(arr):
    return sum(num if not i % 2 else num**2 for i, num in enumerate(arr))
