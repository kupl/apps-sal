def close_compare(a, b, margin=0):
    dif = a-b
    return 0 if abs(dif)<=margin else -1 if dif<0 else 1
