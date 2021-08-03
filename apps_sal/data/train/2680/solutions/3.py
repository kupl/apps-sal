def race(v1, v2, g):
    if v1 >= v2:
        return None
    t = float(g) / (v2 - v1) * 3600
    mn, s = divmod(t, 60)
    h, mn = divmod(mn, 60)
    return [int(h), int(mn), int(s)]
