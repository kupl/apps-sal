def close_compare(a, b, margin=0):
    if a >= b:
        res = a - margin
        if res <= b:
            return 0
        else:
            return 1
    if a <= b:
        ress = b - margin
        if ress <= a:
            return 0
        else:
            return -1
