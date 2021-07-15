def nth_smallest(arr, pos):
    for i in range(pos):
        result = min(arr)
        arr.remove(result)
    return result
