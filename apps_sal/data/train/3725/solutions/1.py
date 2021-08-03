def shift_left(a, b):
    r = 0
    while a != b:
        if len(b) > len(a):
            b = b[1::]
            r += 1
        else:
            a = a[1::]
            r += 1

    return r
