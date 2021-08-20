def int_diff(arr, n):
    return sum((1 for (i, x) in enumerate(arr[:-1]) for y in arr[i + 1:] if abs(y - x) == n))
