def get_chance(n, x, a):
    p = 1
    for i in range(a):
        p = p * (n - x - i) / (n - i)
    return float("{:.2f}".format(p) if p < 1 else 0.0)
