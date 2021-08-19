def close_compare(a, b, c=0):
    return ((a > b) - (b > a)) * (abs(a - b) > c)
