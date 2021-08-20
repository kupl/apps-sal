def close_compare(a, b, margin=0):
    if margin == None:
        margin = 0
    elif margin >= abs(a - b):
        return 0
    elif a < b:
        return -1
    else:
        return 1
