def micro_world(bacteria, k):
    b = sorted(bacteria)
    (f, leng) = (0, len(b))
    for (i, e) in enumerate(b[:-1]):
        if e < b[i + 1] and e + k >= b[i + 1]:
            leng = leng - 1 - f
            f = 0
        elif e == b[i + 1]:
            f += 1
        else:
            f = 0
    return leng
