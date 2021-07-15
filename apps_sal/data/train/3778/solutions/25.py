def find_smallest_int(arr):
    l = len(arr)
    min = arr[0]
    for i in range(1, l):
        if min > arr[i]:
            min = arr[i]
    return min
