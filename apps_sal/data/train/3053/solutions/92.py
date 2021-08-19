def close_compare(a, b, margin=0):
    diff = abs(a - b)
    if margin >= diff:
        return 0
    elif a < b:
        return -1
    else:
        return 1
