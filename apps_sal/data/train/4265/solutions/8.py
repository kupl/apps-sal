def tops(m, n=1): return (lambda q: "" if q > len(m) else tops(m, n + 1) + m[q])(2 * n * n - n)
