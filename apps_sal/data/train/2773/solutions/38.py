def calculate_years(P, I, T, D):
    total = []
    while P < D:
        x = P * I
        y = x * T
        z = P + (x - y)
        total.append(z)
        P = z
    return len(total)
