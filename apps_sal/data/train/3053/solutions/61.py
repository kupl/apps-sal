def close_compare(a, b, margin = 0):
    if a < b and a + margin < b: return -1
    if b < a and b + margin < a: return 1
    return 0
