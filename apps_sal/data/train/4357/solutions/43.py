def nth_smallest(arr, pos):
    sort = sorted(arr,reverse=True)
    return sort[-pos]
