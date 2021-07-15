def close_compare(a, b, margin=0):
    if a < b:
        res = -1
    elif a > b:
        res = 1
    if margin >= abs(b - a):
        res = 0
    return res
