def sequence_sum(a, b, s):
    n = (b - a) // s
    return 0 if n < 0 else (n + 1) * (2 * a + s * n) // 2
