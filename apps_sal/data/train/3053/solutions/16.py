def close_compare(a, b, margin=0):
    return a - b > margin or -(a - b < -margin)
