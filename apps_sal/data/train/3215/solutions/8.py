def reduce_pyramid(base):
    sm = 0
    nb = 1
    for (i, u) in enumerate(base, 1):
        sm += nb * u
        nb = nb * (len(base) - i) // i
    return sm
