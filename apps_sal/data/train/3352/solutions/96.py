def find_longest(arr):
    ret = arr[0]
    for x in arr:
        if len(str(x)) > len(str(ret)):
            ret = x
    return ret
