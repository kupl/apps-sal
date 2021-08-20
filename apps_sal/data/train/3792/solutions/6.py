def slogans(p, r):
    c = 0
    while r:
        for i in range(len(p)):
            if r.startswith(p[i:]):
                c += 1
                r = r[len(p[i:]):]
                break
    return c
