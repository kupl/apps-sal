def find_smallest_int(arr):
    s = arr[0]
    for i in arr[1:]:
        if i < s:
            s = i
    return s
