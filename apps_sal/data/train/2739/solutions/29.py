def cube_odd(arr):
    res = 0
    for i in arr:
        if type(i) != int:
            return None
        if i % 2:
            res += i ** 3
    return res
