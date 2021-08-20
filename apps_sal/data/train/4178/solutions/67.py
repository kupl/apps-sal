def min_sum(arr):
    arr = sorted(arr)
    return sum((arr[x - 1] * arr[-x] for x in range(1, len(arr) // 2 + 1)))
