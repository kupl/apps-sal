def nth_smallest(arr, pos):
    arr.sort()
    newPos = pos - 1
    nSmall = arr[newPos]
    return nSmall
