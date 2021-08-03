def nth_smallest(arr, pos):
    newlis = []
    newlis = list(arr)
    newlis.sort()
    return(newlis[pos - 1])
