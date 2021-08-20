def cube_odd(arr):
    n = 0
    for i in arr:
        if type(i) != int:
            return None
            break
        elif i % 2 != 0 or -1 * i % 2 != 0:
            n += i ** 3
    return n
