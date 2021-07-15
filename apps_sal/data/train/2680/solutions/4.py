def race(v1, v2, g):
    if v1 < v2:
        sec = g * 60 * 60 // (v2 - v1)
        return [sec // 3600, sec // 60 % 60, sec % 60]
