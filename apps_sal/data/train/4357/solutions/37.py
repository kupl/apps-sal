def nth_smallest(arr, pos):
    sar = sorted(arr)
    return sar.pop(pos - 1)
