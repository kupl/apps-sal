def close_compare(a, b, margin=0):
    return [-1, 1, 0][-(abs(a - b) <= margin) + (a > b + margin)]
