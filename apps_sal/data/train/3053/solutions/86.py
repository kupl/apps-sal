def close_compare(a, b, margin=0):
    if abs(b - a) <= abs(margin):
        return 0
    if a > b:
        return 1
    return -1
