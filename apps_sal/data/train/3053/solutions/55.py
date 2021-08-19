def close_compare(a, b, margin=0):
    dif = a - b
    if abs(dif) <= margin:
        return 0
    elif dif < 0:
        return -1
    else:
        return 1
