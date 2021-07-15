def hamming_weight(x):
    w = 0
    while x:
        w += x & 1
        x >>= 1
    return w
