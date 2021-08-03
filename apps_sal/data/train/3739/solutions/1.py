def branch(n): return (lambda r: r and (n - 2) // r + 2 - r)(0 - (1 - n**.5) // 2 * 2)
