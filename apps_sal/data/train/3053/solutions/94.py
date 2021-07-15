def close_compare(a, b, margin=0):
    return (abs(a - b) > margin) * (-1) ** (a < b)
