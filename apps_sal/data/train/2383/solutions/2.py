import math
import sys
t = int(input())
for i in range(t):
    (a, b) = list(map(int, input().split()))
    if a > b:
        (a, b) = (b, a)
    s = max(b, a * 2)
    print(s * s)
