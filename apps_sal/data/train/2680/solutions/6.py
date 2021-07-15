def race(v1, v2, g):
    if v1 < v2:
        a = g * 3600 // (v2 - v1)
        return [a // 3600, a // 60 % 60, a % 60]
