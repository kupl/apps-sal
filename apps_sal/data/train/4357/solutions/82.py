def nth_smallest(arr, pos):
    result = None
    if pos <= len(arr):
        arr.sort()
        result = arr[(pos - 1):][0]
    return result
