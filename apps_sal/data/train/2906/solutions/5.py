def generate_number(squad, n):
    x, squad = n, set(squad)
    for d in range(1, 10):
        if x not in squad:
            return x
        if 0 < n - d < 10:
            x = 9 * d + n
    if x not in squad:
        return x
