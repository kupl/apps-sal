(a, b) = list(map(int, input().split()))
dangbra = b * (b - 1) // 2 * (a * (a + 1) // 2) * b + b * (b - 1) // 2 * a
print(int(dangbra % 1000000007))
