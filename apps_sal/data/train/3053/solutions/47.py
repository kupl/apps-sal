def close_compare(a, b, margin=0):
    if margin == 0:
        if a == b:
            return 0
        elif a > b:
            return 1
        elif a < b:
            return -1
    elif margin > 0:
        if a - b > 0 and a - b <= margin:
            return 0
        elif a - b < 0 and (a - b) * -1 == margin:
            return 0
        elif a - b < 0 and (a - b) * -1 <= margin:
            return 0
        elif a == b:
            return 0
        elif a > b:
            return 1
        elif a - b < 0 and a - b <= margin:
            return -1
