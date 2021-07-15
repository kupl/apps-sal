def nth_smallest(arr, n):
    if n == 1:
        return min(arr)
    del arr[arr.index(min(arr))]
    return nth_smallest(arr, n-1)
