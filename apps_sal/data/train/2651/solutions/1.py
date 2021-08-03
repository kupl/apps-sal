def prod2sum(a, b, c, d):
    r1 = sorted([abs(a * c - b * d), abs(a * d + b * c)])
    r2 = sorted([abs(a * c + b * d), abs(a * d - b * c)])
    return sorted([r1, r2]) if r1 != r2 else [r1]
