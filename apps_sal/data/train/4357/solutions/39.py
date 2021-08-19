def nth_smallest(arr, pos):
    # sort array
    arr.sort()

    # get smallest
    nthSmallest = arr[pos - 1]

    return nthSmallest
