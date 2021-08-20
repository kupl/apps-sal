def close_compare(a, b, margin=0):
    if a - b >= 0 and a - b <= margin:
        return 0
    elif b - a >= 0 and b - a <= margin:
        return 0
    elif a < b:
        return -1
    else:
        return 1
