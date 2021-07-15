def close_compare(a, b, margin=0):
    if abs(a - b) > margin:
        return 1 - 2 * (a < b)
    else:
        return 0
