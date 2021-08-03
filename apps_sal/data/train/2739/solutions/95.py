def cube_odd(arr):
    r = 0
    for a in arr:
        if type(a) != int:
            return None
        if a % 2 != 0:
            r += a**3
    return r
