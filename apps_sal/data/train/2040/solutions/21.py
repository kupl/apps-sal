n, h = map(int, input().split())
from math import sqrt
for i in range(n - 1):
    print(h * sqrt((i + 1) / n), end = ' ')

