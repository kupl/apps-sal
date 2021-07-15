def find_smallest_int(arr):
    min = arr[0]
    for pos in arr:
        if pos < min:
            min = pos
    return min
