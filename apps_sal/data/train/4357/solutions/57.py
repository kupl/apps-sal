def nth_smallest(arr, pos):
    arr.sort()
    # print(arr)
    return arr[pos - 1]
