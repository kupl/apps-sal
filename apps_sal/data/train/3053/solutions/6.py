from numpy import sign


def close_compare(a, b, margin=0):
    return abs(a - b) > margin and sign(a - b)
