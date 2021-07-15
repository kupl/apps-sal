def close_compare(a=0, b=0, margin=0):
    return 0 if abs(a - b) <= margin else -1 if b > a else 1
