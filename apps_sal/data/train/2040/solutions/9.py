from math import sqrt
n, h = map(int, input().split())
h = h * 1.00
l = []
for i in range(0, 1500):
    l.append(sqrt(i))
area = sqrt((h * h) / n)
for i in range(1, n):
    print(l[i] * area, end=" ")
