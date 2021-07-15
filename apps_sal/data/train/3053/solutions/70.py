def close_compare(a, b, margin=0):
    d = abs(a - b)
    if d <= margin:
        return 0
    elif a < b:
        return -1
    return 1

