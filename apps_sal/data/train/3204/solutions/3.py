def Guess_it(n, m):
    return [[g, r, n - g - r] for g in range(n + 1) for r in range(n - g + 1) if (n - g - r) * 3 + r * 4 + g * 5 == m]
