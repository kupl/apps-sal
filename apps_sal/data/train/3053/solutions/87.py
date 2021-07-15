def close_compare(a, b, margin=0):
    if margin >= abs(a-b):
        return 0
    if a > b:
        return 1
    elif b > a:
        return -1

