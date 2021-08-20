def nth_smallest(arr, pos):
    arr.sort()
    nthSmallest = arr[pos - 1]
    return nthSmallest
