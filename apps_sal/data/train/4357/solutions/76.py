def nth_smallest(arr, pos):
    arr.sort()
    [arr.pop(0) for _ in range(pos-1)] 
    return arr[0]
