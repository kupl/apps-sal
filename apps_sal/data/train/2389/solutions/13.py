from heapq import heappush, heappop
from collections import deque, Counter, defaultdict
import itertools
import sys
sys.setrecursionlimit(10 ** 6)


def MI():
    return list(map(int, input().split()))


def I():
    return int(input())


def LI():
    return [int(i) for i in input().split()]


YN = ['YES', 'NO']
input = sys.stdin.readline
q = I()
for _ in range(q):
    (n, k) = LI()
    ans = k
    s = list(input())
    l = 'RGB'
    c = [[0], [0], [0]]
    for i in range(n):
        for j in range(3):
            if s[i] != l[(i + j) % 3]:
                c[j].append(c[j][-1] + 1)
            else:
                c[j].append(c[j][-1])
    for i in range(n - k + 1):
        for j in range(3):
            ans = min(c[j][i + k] - c[j][i], ans)
    print(ans)
