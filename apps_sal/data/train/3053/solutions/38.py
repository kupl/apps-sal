def close_compare(a, b, margin=0):
    if a < b and abs(a - b) > margin:
        return -1
    elif a == b or abs(a - b) <= margin:
        return 0
    else:
        return 1
