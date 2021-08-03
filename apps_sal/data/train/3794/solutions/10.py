def nth_smallest(arr, n):
    arr = sorted(list(set(arr)))
    if n > len(arr):
        return None
    return arr[n - 1]
