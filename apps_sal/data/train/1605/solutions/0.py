a, b = map(int, input().split())
print(((b - 1) * a * b // 2 + (a + 1) * a * b * b * (b - 1) // 4) % 1000000007)
