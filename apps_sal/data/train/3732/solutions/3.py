def is_madhav_array(arr):
    if len(arr) < 3:
        return False
    (i, n) = (0, 1)
    value = arr[0]
    while i + n <= len(arr):
        if sum(arr[i:i + n]) != value:
            return False
        i += n
        n += 1
    return i == len(arr)
