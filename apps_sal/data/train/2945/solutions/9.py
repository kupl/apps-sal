fortune = F = lambda f, p, c, n, i: F(f * (100 + p) // 100 - c, p, c * (100 + i) // 100, n - 1, i)if n > 1else f >= 0
