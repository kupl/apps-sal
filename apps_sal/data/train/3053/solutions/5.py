def close_compare(a, b, margin=0):
    return abs(a-b) > margin and (a>b) - (a<b)
