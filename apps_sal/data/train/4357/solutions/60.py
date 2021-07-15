def nth_smallest(arr, pos):
    for _ in range(pos-1):
        arr.remove(min(arr))
        
    return min(arr)
