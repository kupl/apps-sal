def find_smallest_int(arr):
    val = arr[0]
    for x in arr:
        if x < val:
            val = x
    return val
