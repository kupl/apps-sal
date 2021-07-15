def close_compare(a, b, margin=0):
    difference = abs(b-a)
    if a < b and difference>margin:
        return -1
    if a > b and difference>margin:
        return 1
    return 0
    pass
