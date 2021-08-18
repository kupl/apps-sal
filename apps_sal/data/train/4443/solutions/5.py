def max_ball(v0):
    g = 9.81

    def h(u):
        return v * u - 0.5 * g * u * u
    v = v0 * 1000 / 3600.0
    t = v / g
    tm = int(t * 10)
    h1 = h(tm / 10.0)
    h2 = h((tm + 1) / 10.0)
    mx = max(h1, h2)
    if (mx == h(tm / 10.0)):
        return tm
    else:
        return tm + 1
