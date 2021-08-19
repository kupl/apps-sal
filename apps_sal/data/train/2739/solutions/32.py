def cube_odd(arr):
    o = 0
    for i in arr:
        if type(i) != int:
            return None
        elif i % 2 == 1:
            o += i ** 3
        else:
            continue
    return o
