def pair_zeros(arr):
    return [d for i, d in enumerate(arr) if d != 0 or arr[:i + 1].count(0) % 2]
