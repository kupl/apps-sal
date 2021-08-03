def close_compare(a, b, margin=0):
    if abs(a - b) <= margin:
        return 0
    elif a < b:
        return -1
    else:
        return 1
