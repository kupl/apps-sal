def gap(g, m, n):
    prev = 2
    for x in range(m|1, n + 1, 2):
        if all(x%d for d in range(3, int(x**.5) + 1, 2)):
            if x - prev == g: return [prev, x]
            prev = x
