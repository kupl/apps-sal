def cube_odd(arr):
    x = 0
    for i in arr:
        if type(i) is not int:
            return None
        if i % 2 != 0:
            x += i*i*i
    return x
