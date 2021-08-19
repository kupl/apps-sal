def isPP(n):
    d = 2
    k = 2
    while d >= 2:
        d = round(n ** (1 / k), 4)
        if d.is_integer():
            return [d, k]
        k += 1
