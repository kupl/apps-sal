def epidemic(tm, n, s0, i0, b, a):
    s = [s0]
    i = [i0]
    r = [0]
    t = 0
    dt = tm / n
    t += dt

    for k in range(n):
        s[k] = s[k - 1] - dt * b * s[k - 1] * i[k - 1]
        i[k] = i[k - 1] + dt * (b * s[k - 1] * i[k - 1] - a * i[k - 1])
        r[k] = r[k - 1] + dt * i[k - 1] * a

        s.append(s[k])
        i.append(i[k])
        r.append(r[k])

    return int(max(i))
