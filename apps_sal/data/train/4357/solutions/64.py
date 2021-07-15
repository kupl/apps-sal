def nth_smallest(arr, pos):
    arr.sort()
    return (0, arr[pos - 1])[pos >= 1]
