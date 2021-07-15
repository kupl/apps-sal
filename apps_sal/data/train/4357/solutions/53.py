def nth_smallest(arr, pos):
    for a in range(pos):
        index = arr.pop(arr.index(min(arr)))
    return index
