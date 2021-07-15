def close_compare(a, b, margin=None):
    if not margin: return -1 if b>a else a>b
    return -1 if b-margin>a else a-margin>b
