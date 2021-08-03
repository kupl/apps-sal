import sys
import math

n, h = map(int, input().split())
for i in range(n - 1):
    print("%f" % (h * math.sqrt((i + 1) / n)), end=" ")
