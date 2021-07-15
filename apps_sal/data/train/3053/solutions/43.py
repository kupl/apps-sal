def close_compare(a, b, margin=0):
    if margin >= abs(a - b):
        return 0
    elif a > b:
        return 1
    elif a < b:
        return -1
    elif a == b:
        return 0
