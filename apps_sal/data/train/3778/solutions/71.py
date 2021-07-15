def find_smallest_int(arr):
    min_val=arr[0]
    for val in arr:
        if val < min_val: min_val=val
    return min_val
