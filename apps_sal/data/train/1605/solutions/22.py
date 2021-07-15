a, b = list(map(int, input().split()))
print((a * b * (b - 1) // 2 + b ** 2 * (b - 1) // 2 * a * (a + 1) // 2) % (10 ** 9 + 7))

