def min_sum(arr):
    arr = sorted(arr)
    return sum([arr[x] * arr[len(arr) - 1 - x] for x in range(len(arr) // 2)])
