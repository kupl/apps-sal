def close_compare(a, b, margin=0):
    if margin is not 0 and abs(a - b) <= margin or a == b:
        return 0
    else:
        return -1 if (a < b) else 1
