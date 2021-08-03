def nth_smallest(arr, pos):
    i = 0
    a = 0
    while i < pos:
        a = min(arr)
        arr.remove(a)
        i += 1
    return a
