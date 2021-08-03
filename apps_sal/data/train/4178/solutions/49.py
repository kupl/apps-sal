def min_sum(arr):
    sarr = sorted(arr)
    return sum(sarr[i] * sarr[-i - 1] for i in range(len(arr) // 2))
