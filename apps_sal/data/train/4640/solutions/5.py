def int_diff(arr, n):
    return sum((sum((abs(a - b) == n for b in arr[i:])) for (i, a) in enumerate(arr, 1)))
