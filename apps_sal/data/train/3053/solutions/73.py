def close_compare(a, b, margin=0):
    return -1 if b-margin>a else a-margin>b
