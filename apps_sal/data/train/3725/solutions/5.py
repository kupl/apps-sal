def shift_left(a, b):
    while True:
        if a and b and a[-1] == b[-1]:
            a, b = a[:-1], b[:-1]
            continue
        return len(a) + len(b)
