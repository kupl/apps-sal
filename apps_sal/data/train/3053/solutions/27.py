def close_compare(a, b, margin=0):
    if a == b or margin >= abs(b - a):
        return 0
    if a < b or margin > abs(a - b):
        return -1
    if a > b or margin < a:
        return 1
