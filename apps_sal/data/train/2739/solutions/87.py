def cube_odd(arr):
    r = 0
    for x in arr:
        if type(x) is not int:
            return None
        elif x % 2:
            r += x ** 3
    return r
    # Flez
