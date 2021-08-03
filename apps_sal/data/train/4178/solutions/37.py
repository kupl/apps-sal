def min_sum(arr):
    total = 0
    while arr:
        m, n = max(arr), min(arr)
        total += arr.pop(arr.index(m)) * arr.pop(arr.index(n))
    return total
