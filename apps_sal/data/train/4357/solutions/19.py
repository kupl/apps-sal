def nth_smallest(arr, pos):
    i = (pos - len(arr) if pos >= len(arr) else pos) - 1
    x = sorted(arr)
    return min(x[i:])
