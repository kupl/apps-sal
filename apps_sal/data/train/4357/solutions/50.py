def nth_smallest(arr, pos):
    arr.sort()
    return list(arr)[pos - 1]
