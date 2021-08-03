def branch(n): return 0 if n == 1 else (lambda s: (n - s * s - 1) // (s + 1))(((n - 1)**0.5 - 1) // 2 * 2 + 1)
