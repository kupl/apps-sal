def find_smallest_int(arr):
    a = 10000
    for i in arr:
        if a > i:
            a = i
    return a
