def close_compare(a, b, margin=0):
    return 1 if a > b and a - b > margin else -1 if a < b and b - a > margin else 0
