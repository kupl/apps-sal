import sys
import math
input = sys.stdin.readline


def binary(l, r, co, b, c):
    x = (l + r) / 2
    val1 = (2 * x + b) * math.sin(x)
    val2 = (x ** 2 + b * x + c) * math.cos(x)
    x = (l + r) / 2
    val = val1 - val2
    if abs(val) < 1e-07 or co == 150:
        return (l + r) / 2
    if val < 0:
        return binary((l + r) / 2, r, co + 1, b, c)
    else:
        return binary(l, (l + r) / 2, co + 1, b, c)


t = int(input())
for _ in range(t):
    (b, c) = list(map(float, input().split()))
    x = binary(1e-10, math.pi / 2 - 1e-10, 0, b, c)
    val = (x * x + b * x + c) / math.sin(x)
    print(val)
