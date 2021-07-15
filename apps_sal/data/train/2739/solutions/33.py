def cube_odd(arr):
    s = 0
    for x in arr:
        if type(x) != int:
            return None
        elif x**3 % 2 == 1:
            s += x**3
    return s

