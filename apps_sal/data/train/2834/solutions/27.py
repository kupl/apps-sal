def symmetric_point(p, q):
    try:
        ((a, b), (c, d)) = (p, q)
        x = c - a + c
        m = (d - b) / (c - a)
        i = b - m * a
        return [x, round(m * x + i)]
    except:
        return [0, 0]
