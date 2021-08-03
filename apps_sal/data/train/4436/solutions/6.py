def S2N(m, n):
    amounts = (lambda x: x + 1,
               lambda x: x * (x + 1) / 2,
               lambda x: x * (x + 1) * (2 * x + 1) / 6,
               lambda x: x**2 * (x + 1)**2 / 4,
               lambda x: x * (x + 1) * (2 * x + 1) * (3 * x**2 + 3 * x - 1) / 30,
               lambda x: x**2 * (x + 1)**2 * (2 * x**2 + 2 * x - 1) / 12,
               lambda x: x * (x + 1) * (2 * x + 1) * (3 * x**4 + 6 * x**3 - 3 * x + 1) / 42,
               lambda x: x**2 * (x + 1)**2 * (3 * x**4 + 6 * x**3 - x**2 - 4 * x + 2) / 24,
               lambda x: x * (x + 1) * (2 * x + 1)
               * (5 * x**6 + 15 * x**5 + 5 * x**4 - 15 * x**3 - x**2 + 9 * x - 3) / 90,
               lambda x: x**2 * (x + 1)**2 * (x**2 + x - 1)
               * (2 * x**4 + 4 * x**3 - x**2 - 3 * x + 3) / 20)
    return sum(amounts[i](m) for i in range(n + 1))
