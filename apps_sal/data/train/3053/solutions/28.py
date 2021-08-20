def close_compare(a, b, margin=None):
    if margin == None:
        margin = 0
    result = a - b
    if margin >= abs(result):
        return 0
    elif result > 0:
        return 1
    else:
        return -1
