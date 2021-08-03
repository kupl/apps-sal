def nb_year(x, p, a, y):
    t = 0
    while True:
        x += x * p / 100 + a
        t += 1
        if x >= y:
            break
    return t
