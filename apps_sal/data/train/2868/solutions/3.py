def is_nice(arr):
    return len(arr) > 0 and all((n - 1 in arr or n + 1 in arr for n in arr))
