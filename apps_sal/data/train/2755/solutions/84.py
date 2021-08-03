def multiple_of_index(arr):
    ret = []
    for val in range(1, len(arr)):
        if arr[val] % (val) == 0:
            ret.append(arr[val])
    return ret
