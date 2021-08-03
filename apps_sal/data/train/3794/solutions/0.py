def nth_smallest(arr, n):
    s = set(arr)
    return sorted(s)[n - 1] if n <= len(s) else None
