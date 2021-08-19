def heron(*l):
    s = sum(l) / 2
    return round((s * (s - l[0]) * (s - l[1]) * (s - l[2])) ** 0.5, 2)
