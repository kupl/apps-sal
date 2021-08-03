def close_compare(a, b, m=0):
    return -1 if a < b and a - b + m < 0 else [0, 1][a > b and m < a - b > 0]
