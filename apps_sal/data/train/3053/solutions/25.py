def close_compare(a, b, margin=0):
    if margin >= abs(a - b):
        return 0
    elif a - b < 0:
        return -1
    else:
        return 1
