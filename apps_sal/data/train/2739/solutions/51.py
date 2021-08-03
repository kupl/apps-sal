def cube_odd(arr):
    res = 0
    for i in arr:
        if not isinstance(i, int) or isinstance(i, bool):
            return None
        elif i % 2 != 0:
            res += i**3
    return res
