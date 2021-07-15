import math

n, h = map(int, input().split())

p = 0
h2n = h * h / n
for _ in range(n - 1):
    x = math.sqrt(h2n + p * p) - p
    p += x
    print(p, end=" ")

