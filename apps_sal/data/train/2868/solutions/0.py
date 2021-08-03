def is_nice(arr):
    s = set(arr)
    return bool(arr) and all(n + 1 in s or n - 1 in s for n in s)
