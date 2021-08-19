def close_compare(a, b, margin=0):
    return (-1 if a < b else 1 if a > b else 0) if margin == 0 else 0 if margin >= abs(a - b) else -1 if a - b < margin else 1
