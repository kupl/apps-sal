def nth_smallest(arr, pos):
    while pos > 0:
        m = min(arr)
        arr.remove(m)
        pos -= 1
    return m
