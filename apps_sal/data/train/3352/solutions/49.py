def find_longest(arr):
    arr_str = map(str, arr)
    res = max(arr_str, key=len)

    return int(res)
