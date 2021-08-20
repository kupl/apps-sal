def f(n):
    (r, c) = ([1], 1)
    for i in range(n):
        c <<= 1
        r.append(c)
    return r + [(c << 1) - 1]
