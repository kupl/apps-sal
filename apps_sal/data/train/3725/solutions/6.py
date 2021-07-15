def shift_left(a, b):
    n = 0
    while not b.endswith(a):
        n += 1
        a = a[1:]
    return n + (len(b) - len(a))
