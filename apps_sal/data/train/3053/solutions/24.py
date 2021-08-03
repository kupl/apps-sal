def close_compare(a, b, margin=None):

    if margin is not None:
        if round(abs(a - b), 3) <= margin:
            return 0

    if a < b:
        return -1
    elif a > b:
        return 1

    return 0
