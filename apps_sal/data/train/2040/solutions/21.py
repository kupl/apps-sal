from math import sqrt
n, h = map(int, input().split())
for i in range(n - 1):
    print(h * sqrt((i + 1) / n), end=' ')
