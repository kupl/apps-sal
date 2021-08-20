def epidemic(tm, n, s0, i0, b, a):
    (dt, imax) = (tm / n, 0)
    (s, i, r) = (s0, i0, 0)
    for _ in range(n):
        (s, i, r) = (s - dt * b * s * i, i + dt * (b * s * i - a * i), r + dt * i * a)
        imax = max(int(i), imax)
    return imax
