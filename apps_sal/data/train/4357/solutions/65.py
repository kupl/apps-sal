def nth_smallest(arr, pos):
    for i in range(len(arr) - pos):
        arr.remove(max(arr))
    return max(arr)
