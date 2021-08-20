def epidemic(tm, n, s, i, b, a):

    def f(s, i, r):
        dt = tm / n
        for t in range(n):
            (s, i, r) = (s - dt * b * s * i, i + dt * (b * s * i - a * i), r + dt * i * a)
            yield i
    return int(max(f(s, i, 0)))
