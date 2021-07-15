def nth_smallest(arr, pos):
    for i in range(pos):
        x = min(arr)
        arr.remove(x)
    return x
