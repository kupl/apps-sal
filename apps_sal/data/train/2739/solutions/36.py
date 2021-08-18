def cube_odd(arr):
    a = 0
    for i in arr:
        if type(i) != int:
            break
        elif i % 2 != 0:
            a += i**3

    else:
        return a
