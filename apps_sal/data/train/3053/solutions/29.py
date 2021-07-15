def close_compare(a, b, margin=None):
    if margin:
        return 0 if  abs(b-a)<=margin else 1 if a>b else -1
    return -1 if a<b else 1 if a>b else 0
