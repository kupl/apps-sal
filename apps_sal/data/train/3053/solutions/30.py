def close_compare(a, b, margin = 0):
    diff = a - b
    if margin >= abs(diff):
        return 0
    return 1 if diff > 0 else -1
