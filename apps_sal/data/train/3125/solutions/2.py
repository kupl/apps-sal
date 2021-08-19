def solve(n):
    return next((((n - x * x) // 2 // x) ** 2 for x in range(int(n ** 0.5), 0, -1) if (n - x * x) % (2 * x) == 0 < n - x * x), -1)
