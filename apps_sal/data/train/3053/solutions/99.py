def close_compare(a, b, margin=0):
    if a == b:
        r = 0
    if a < b:
        r = -1
    if a > b:
        r = 1
    if abs(a - b) <= margin:
        r = 0
    return r
