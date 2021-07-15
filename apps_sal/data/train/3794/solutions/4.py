def nth_smallest(arr, n):
    s = set(arr)
    return None if len(s) < n else sorted(s)[n-1]
