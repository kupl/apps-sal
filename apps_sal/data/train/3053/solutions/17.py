def close_compare(a, b, margin=0):
    return (2 * (a > b) - 1) * (abs(a - b) > margin)
