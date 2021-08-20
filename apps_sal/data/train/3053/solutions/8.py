def close_compare(a, b, m=0):
    return 0 if abs(a - b) <= m else -1 * (a < b) + (a > b)
