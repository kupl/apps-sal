(a, b) = map(int, input().split())
print((((b * a * (a + 1) >> 1) + a) * (b - 1) * b >> 1) % 1000000007)
