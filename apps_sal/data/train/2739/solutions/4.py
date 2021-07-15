def cube_odd(arr):
    s = 0
    for n in arr:
        if type(n) != int: break
        elif n%2: s += n**3
    else:
        return s
