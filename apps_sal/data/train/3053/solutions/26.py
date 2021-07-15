def close_compare(a, b, margin=0):
    x = a - b
    if margin >= abs(x):
        return 0
    elif x < 0:
        return -1
    else:
        return 1
