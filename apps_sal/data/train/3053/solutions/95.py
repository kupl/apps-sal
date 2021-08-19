def close_compare(a, b, margin=0):
    if abs(a - b) > margin:
        return 1 if a - b > 0 else -1
    return 0
