def nth_smallest(arr, n):
    x = list(dict.fromkeys(arr))
    x.sort(key=int)
    return None if n > len(x) else x[n - 1]
