def close_compare(a, b, margin=0):
    if margin > 0:
        if abs(a - b) <= margin:
            return 0
        else:
            if a - b > 0:
                return 1
            else:
                return -1
    else:
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0

