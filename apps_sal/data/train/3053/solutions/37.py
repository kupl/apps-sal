def close_compare(a, b, margin=0):
    difference = abs(a - b)
    if margin >= difference:
        return 0
    elif a > b:
        return 1
    elif a < b:
        return -1
    pass
