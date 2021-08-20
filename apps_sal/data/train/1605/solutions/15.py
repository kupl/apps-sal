(a, b) = map(int, input().split())
print((b - 1) * b // 2 * (b * a * (a + 1) // 2 + a) % (10 ** 9 + 7))
