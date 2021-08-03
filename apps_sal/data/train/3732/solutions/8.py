def is_madhav_array(arr):
    if len(arr) <= 2:
        return False
    i, k = 0, 1
    while i + k <= len(arr):
        if arr[0] != sum(arr[i: i + k]):
            return False
        if i + k == len(arr):
            return True
        i += k
        k += 1
    return False
