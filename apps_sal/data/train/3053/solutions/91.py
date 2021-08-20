def close_compare(a, b, margin=0):
    if margin == 0:
        if a > b:
            return 1
        elif b > a:
            return -1
        else:
            return 0
    elif a > b and a - b > margin:
        return 1
    elif a < b and b - a > margin:
        return -1
    else:
        return 0
