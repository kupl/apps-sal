def get_chance(n, x, a):
    prob = 1
    while a:
        prob *= (n - x) / n
        n -= 1
        a -= 1
    return round(prob, 2)
