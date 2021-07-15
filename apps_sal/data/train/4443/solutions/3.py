def max_ball(v0, g=9.81):
    v = v0 / 3.6
    prev = 0
    for i in range(1000):
        t = i * 0.1
        h = v*t - 0.5*g*t*t
        if h < prev:
            return i - 1
        prev = h
