def epidemic(tm, n, s0, i0, b, a):

    def evolve():
        (s, i, r, dt) = (s0, i0, 0, tm / n)
        while 1:
            (s, i, r) = (s - dt * b * s * i, i + dt * (b * s * i - a * i), r + dt * i * a)
            yield i
    for i1 in evolve():
        if i1 < i0:
            return i0
        i0 = i1
