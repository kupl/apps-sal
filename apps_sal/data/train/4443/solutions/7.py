def max_ball(v0):
    v = v0 * (1000 / 3600)
    g = 9.81
    t = 0
    record = []
    while v * t - 0.5 * g * t * t >= 0:
        h = v * t - 0.5 * g * t * t
        record.append(h)
        t += 0.1
    return record.index(max(record))
