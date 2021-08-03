def cube_odd(arr):
    s = 0
    for i in arr:
        if type(i) is int:
            if i % 2 != 0:
                s += i ** 3
        else:
            return None
    return s
