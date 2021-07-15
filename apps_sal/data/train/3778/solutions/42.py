def find_smallest_int(arr):
    ret = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < ret:
            ret = arr[i]
    return ret
