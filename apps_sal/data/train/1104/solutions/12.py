import math
from sys import stdin, stdout
from math import gcd, sqrt, ceil, floor, inf
from copy import deepcopy
def ii1(): return int(stdin.readline().strip())
def is1(): return stdin.readline().strip()


def iia(): return list(map(int, stdin.readline().strip().split()))
def isa(): return stdin.readline().strip().split()


mod = 1000000007
for _ in range(ii1()):
    n, k = iia()
    new = k - 1
    if n == 0:
        if k == 1:
            ans = 0
        else:
            ans = (k - 1) * (k)
    elif k == 1:
        ans = n * (n + 1) - n
    elif k % 2 == 0:
        ans = (n + (new // 2)) * (n + (new // 2) + 1) + n
    else:
        ans = (n + (new // 2)) * (n + (new // 2) + 1) - n
    print(ans % mod)
