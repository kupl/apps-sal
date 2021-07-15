def close_compare(a, b, margin = 0):
    abs(margin)
    if a < b and b - a <= margin:
        return 0
    elif a > b and a - b <= margin:
        return 0
    elif a == b and a - b <= margin:
        return 0
    elif a < b:
        return -1
    else:
        return 1
