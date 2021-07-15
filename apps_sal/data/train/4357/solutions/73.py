def nth_smallest(arr, pos):
    i = pos
    while i > 0:
        result = min(arr)
        arr.remove(min(arr))
        i -= 1
    return result
        
        

