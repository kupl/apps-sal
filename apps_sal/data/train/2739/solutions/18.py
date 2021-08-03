def cube_odd(a):
    sum, i = 0, 0
    while True:
        try:
            if type(a[i]) != int:
                return None
            if a[i] & 1:
                sum += a[i]**3
        except IndexError:
            break
        i += 1
    return sum
