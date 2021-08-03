def find_smallest_int(arr):
    small = arr[0]
    for n in arr:
        if n < small:
            small = n
    return small
