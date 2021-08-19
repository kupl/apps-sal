def find_closest_value(m):

    def a(i):
        return (i - 1) // 4 * 65 + [4, 9, 56, 61][(i - 1) % 4]

    def s(n):
        return a(-~((n * n - 1) // 2)) + (4 if n % 2 == 0 else 0)
    n = int((m // 65 * 8) ** 0.5)
    while s(n) <= m:
        n += 1
    if n == 1:
        return 4
    d1 = s(n) - m
    d2 = m - s(n - 1)
    return s(n) if d1 <= d2 else s(n - 1)
