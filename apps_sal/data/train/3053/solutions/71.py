def close_compare(a, b, margin=0):
    if a == b or abs(a - b) <= margin or abs(b - a) <= margin:
        return 0
    elif a > b:
        return 1
    else:
        return -1
