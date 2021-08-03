def close_compare(a, b, margin=0):
    if margin == 0:
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0
    else:
        c = 0
        c = a - b
        if c == 0:
            return 0
        elif a > b and c <= margin:
            return 0
        elif a < b and abs(c) <= margin:
            return 0
        elif a > b and c > margin:
            return 1
        else:
            return -1
