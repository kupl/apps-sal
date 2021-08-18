
import sys
import os
import math


n, h = map(int, input().split())

X = []
for i in range(1, n):
    c = math.sqrt(i / n) * h
    X.append(c)

print(*X)
