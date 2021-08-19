def race(v1, v2, g):
    if v1 >= v2:
        return None
    t = g / (v2 - v1) * 60 * 60
    return [int(t // 3600), int(t // 60 % 60), int(t % 60)]
