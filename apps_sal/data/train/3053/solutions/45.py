def close_compare(a, b, margin=0):
    if abs(b - a) <= margin:
        return 0
    elif b > a:
        return -1
    else:
        return 1
