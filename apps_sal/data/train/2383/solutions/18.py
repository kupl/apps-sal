import math
from math import gcd
t = int(input())
cnt = 0
ans = 0
for i in range(t):
    (a, b) = map(int, input().split())
    if 2 * min(a, b) > max(a, b):
        print((2 * min(a, b)) ** 2)
    else:
        print(max(a, b) ** 2)
