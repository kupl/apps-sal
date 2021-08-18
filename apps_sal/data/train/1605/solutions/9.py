a, b = map(int, input().split())

nicesum = (b * (b - 1) // 2) * (a * (a + 1) // 2) * b + (b * (b - 1) // 2) * a

print(int(nicesum % 1000000007))
