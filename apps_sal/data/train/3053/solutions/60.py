def close_compare(a, b, margin=0):
    closer = abs(b - a)
    if margin >= closer:
        return 0
    elif a > b:
        return 1
    else:
        return -1
