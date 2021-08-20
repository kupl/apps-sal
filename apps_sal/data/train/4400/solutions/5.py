def minimum_steps(num, v):
    (n, s) = (0, 0)
    while s < v:
        s += sorted(num)[n]
        n += 1
    return n - 1
