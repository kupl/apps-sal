from collections import Counter, defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline


def solve():
    n = int(input())

    c = [0] * (10**6 + 1000)
    for el in (int(x) for x in input().split()):
        c[el] += 1
    res = 0
    for i in range(10**6 + 999):
        c[i + 1] += c[i] // 2
        res += c[i] % 2
    print(res)


tt = 1
for test in range(tt):
    solve()
