def close_compare(a, b, margin=0):
    if margin == None:
        margin = 0
    else:
        if margin >= abs(a - b):
            return 0
        else:
            if a < b:
                return -1
            else:
                return 1
