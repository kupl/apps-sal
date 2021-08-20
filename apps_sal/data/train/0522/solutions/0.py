from math import sqrt, ceil, floor
import sys


def get_array():
    return list(map(int, sys.stdin.readline().strip().split()))


def get_ints():
    return list(map(int, sys.stdin.readline().strip().split()))


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)
n = int(input())
co = 0
ans = 0
for i in range(1, n):
    ans += n // i
    if n % i == 0:
        ans -= 1
print(ans)
