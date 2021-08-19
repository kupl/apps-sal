def convert(n):
    r = [0, 0]
    for (i, d) in enumerate(str(n)[::-1]):
        if i % 4 == 0:
            r[0] += int(d)
        elif i % 4 == 2:
            r[0] -= int(d)
        elif i % 4 == 1:
            r[1] += int(d)
        else:
            r[1] -= int(d)
    return r
