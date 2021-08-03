import math
k, n = map(int, input().split())
x = 10**9 + 7
print((math.factorial(n + k - 1) // (math.factorial(k - 1) * math.factorial(n))) % x)
