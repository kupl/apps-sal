import math
import sys
from collections import Counter


def add(x, y):
    cnt = 0
    while y > 0:
        u = x ^ y
        v = x & y
        x = u
        y = v * 2
        cnt += 1
    return cnt


T = int(input())
for _ in range(0, T):
    a = input()
    b = input()
    print(add(int(a, 2), int(b, 2)))
