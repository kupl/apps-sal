def nth_smallest(arr, pos):
    ref = pos - 1
    arr.sort(reverse=False)
    return arr[ref]
