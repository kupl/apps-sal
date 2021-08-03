def sol_equa(n):
    f = [[i, n // i] for i in range(1, int(n**0.5) + 1) if not n % i]
    return [[(a + b) // 2, (b - a) // 4] for (a, b) in f if ((a + b) // 2)**2 - 4 * ((b - a) // 4)**2 == n]
