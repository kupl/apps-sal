import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

import math
import collections
from sys import stdin, stdout, setrecursionlimit
import bisect as bs
setrecursionlimit(2**20)
M = 10**9 + 7

# T = int(stdin.readline())
T = 1

for _ in range(T):
    # n = int(stdin.readline())
    n, a, b = list(map(int, stdin.readline().split()))
    # h = list(map(int,stdin.readline().split()))
    # q = int(stdin.readline())
    # a = list(map(int,stdin.readline().split()))
    # b = list(map(int,stdin.readline().split()))
    if(a > (n - 1)):
        print(n + 1)
        continue
    if(b - a - 2 > 0):
        ans = a
        op = n - (a - 1)
        ans += (op // 2) * (b - a)
        ans += (op % 2)
        print(ans)
        continue
    print(n + 1)
