def reduce_pyramid(base):
    s, c = 0, 1
    for i, x in enumerate(base, 1):
        s += c * x
        c = c * (len(base) - i) // i
    return s
