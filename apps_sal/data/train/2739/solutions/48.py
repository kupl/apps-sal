def cube_odd(arr):
    x = 0
    for i in arr:
        if type(i) is not int:
            return None
            break
        elif i % 2 != 0:
            x += i**3
    return x
