def close_compare(a, b, m=0):
    return [(a > b) - (a < b), 0][abs(a - b) <= m]
