def close_compare(a, b, margin=0):
    if abs(margin) > abs(a - b):
        return 0
    elif abs(margin) > abs(a - b):
        if a > b:
            return 1
        elif a < b:
            return -1
    elif abs(margin) == abs(a - b):
        return 0
    elif a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
