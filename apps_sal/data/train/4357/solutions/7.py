def nth_smallest(arr, pos):
    arr.sort()

    # Return k'th element in the
    # sorted array
    return arr[pos - 1]
