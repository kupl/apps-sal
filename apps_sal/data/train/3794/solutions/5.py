def nth_smallest(arr, n):
    s = set(arr)
    if n <= len(s):
        return sorted(s)[n-1]
