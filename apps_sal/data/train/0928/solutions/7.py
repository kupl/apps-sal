import sys
from math import gcd
def input(): return sys.stdin.readline().strip()


def inp(): return list(map(int, sys.stdin.readline().strip().split()))


for _ in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        d = i * i
        if d > n:
            break
        if d % 3 != 0:
            ans += 1
    print(ans)
