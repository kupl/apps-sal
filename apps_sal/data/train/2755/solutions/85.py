def multiple_of_index(arr):
    ret = []
    for val in range(len(arr) - 1):
        if arr[val + 1] % (val + 1) == 0:
            ret.append(arr[val + 1])
    return ret
