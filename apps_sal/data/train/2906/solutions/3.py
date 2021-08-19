def generate_number(squad, n):
    (l, d) = (n - 1, 9 + n) if n < 11 else (19 - n, n * 10 - 81)
    return next((d + i * 9 for i in range(l) if d + i * 9 not in squad), None) if n in squad else n
