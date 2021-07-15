def find_smallest_int(arr):
    x = arr[0]
    for num in arr:
        if num < x:
            x = num
        else:
            pass
    return x
