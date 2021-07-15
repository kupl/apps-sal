def close_compare(a, b, margin=0):
    adiff = abs(a-b)
    if adiff <= margin:
        return 0
    alist = sorted([a, b])
    if alist[0] == a:
        return -1
    else:
        return 1


