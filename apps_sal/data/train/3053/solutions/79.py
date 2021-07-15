def close_compare(a, b, margin=0):
    if a-b>margin:
        return 1
    elif a+margin<b:
        return -1
    else:
        return 0
