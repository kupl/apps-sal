def reduce_pyramid(b):
    (p, r) = (1, b[0])
    for i in range(1, len(b)):
        p = p * (len(b) - i) // i
        r += b[i] * p
    return r
