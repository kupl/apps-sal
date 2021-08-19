def max_ball(v0):
    # acceleration
    g = 9.81
    # height from ground, u is time in s, v speed in m/s

    def h(u):
        return v * u - 0.5 * g * u * u
    # from km/h to m/s
    v = v0 * 1000 / 3600.0
    # in t = v/g the derivative is 0, the height is max
    t = v / g
    # record done every 0.1 s; tm is in tenth of second
    tm = int(t * 10)
    # device max is before (<=) or after tm (>)
    h1 = h(tm / 10.0)
    h2 = h((tm + 1) / 10.0)
    mx = max(h1, h2)
    # is the recorded max before or after the theoric max
    if (mx == h(tm / 10.0)):
        return tm
    else:
        return tm + 1
