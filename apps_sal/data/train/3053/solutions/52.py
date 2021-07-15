def close_compare(a, b, m=0):
    d = a-b
    if abs(d) <= m: return 0
    return d/abs(d)
