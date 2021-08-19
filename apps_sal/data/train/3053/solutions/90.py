def close_compare(a, b, m=0):
    return 0 if abs(a - b) <= m else (a - b) // abs(a - b)
