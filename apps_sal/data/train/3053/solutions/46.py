def close_compare(a, b, margin=0):
    if a > b:
        d = a-b
        return 1 if d>margin else 0
    elif b > a:
        d = b-a
        return -1 if d>margin else 0
    else:
        return 0
