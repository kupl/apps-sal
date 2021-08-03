def close_compare(a, b, m=0):
    return -1 if m + a < b else [0, 1][m + b < a]
