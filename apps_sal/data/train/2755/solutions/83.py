def multiple_of_index(arr):
    num = 1
    ret = []
    for i in arr[1:]:
        if i % num == 0:
            ret.append(i)
        num = num + 1
    return ret
