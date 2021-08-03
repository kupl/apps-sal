def epidemic(tm, n, s0, i0, b, a):
    from math import floor
    S, I = [s0], [i0]

    dt = tm / n
    for _ in range(n):
        s = S[-1] - dt * b * S[-1] * I[-1]
        i = I[-1] + dt * (b * S[-1] * I[-1] - a * I[-1])
        S.append(s)
        I.append(i)
    return int(max(I))
