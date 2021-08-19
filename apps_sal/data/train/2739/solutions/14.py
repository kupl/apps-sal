def cube_odd(arr):
    # your code here - return None if at least a value is not an integer
    n = 0
    for i in arr:
        if type(i) != int:
            return None
            break
        else:
            if i % 2 != 0 or (-1 * i) % 2 != 0:
                n += i**3
    return n
