def close_compare(a, b, margin=0):
    if max(a, b) - min(a, b) <= margin:
        return 0
    if a > b:
        return 1
    return -1
