def nth_smallest(arr, pos):
    arr.sort()
    for i in range(len(arr)):
        if i + 1 == pos:
            return arr[i]
