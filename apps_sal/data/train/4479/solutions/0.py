def elements_sum(arr, d=0):
    return sum(r[i] if i < len(r) else d for i, r in enumerate(reversed(arr)))
