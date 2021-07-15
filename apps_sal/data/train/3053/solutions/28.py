def close_compare(a, b, margin=None):
    # None is required when there is optional argument
    if margin == None:
        margin = 0
    # cheking difference between a and b
    result = a - b
    # if close to margin
    if margin >= abs(result):
        return 0
    elif result > 0:
        return 1
    else:
        return -1
