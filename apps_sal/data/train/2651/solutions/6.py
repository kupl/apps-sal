def prod2sum(a, b, c, d):
    return sorted(map(list, {tuple(sorted(map(abs, s))) for s in ((a * c - b * d, a * d + b * c), (a * d - b * c, a * c + b * d))}))
