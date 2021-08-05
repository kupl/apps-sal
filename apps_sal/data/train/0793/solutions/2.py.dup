from math import fabs
import sys
sys.setrecursionlimit(10**6)


def f(x):
    return int(fabs(x - r))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n, r = map(int, input().split())
li = list(map(int, input().split()))
li = list(map(f, li))
result = li[0]
for i in li[1:]:
    result = gcd(result, i)
print(result)
