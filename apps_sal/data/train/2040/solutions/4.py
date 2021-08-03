from math import sqrt
n, h = map(int, input().split())
s = []
for i in range(1, n):
    s.append(h * sqrt(i / n))
print(*s)
