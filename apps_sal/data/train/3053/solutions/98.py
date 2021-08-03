def close_compare(a, b, margin=0):
    out = 0
    if a > b:
        out = 1
    else:
        out = -1
    if margin >= abs(a - b):
        out = 0
    return out
