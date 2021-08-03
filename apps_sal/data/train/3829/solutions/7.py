def build_square(B): return (lambda a, b, c, d: 15 < a + b * 2 + 3 * min(a, c) + d * 4)(*map(B.count, (1, 2, 3, 4)))
