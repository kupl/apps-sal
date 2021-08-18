import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)


def input():
    return sys.stdin.readline()[:-1]


mod = 10**9 + 7


def I(): return int(input())
def LI(): return list(map(int, input().split()))


def LIR(row, col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))


N = I()
a = LI()

asort = sorted(a)

d = defaultdict(int)
for i in range(N):
    d[a[i]] += 1
keys = sorted(list(d.keys()))

ans = [0] * N
max_ = 0
place = 0
for i in range(N):
    if a[i] > max_:
        diff = a[i] - max_
        num = N - bisect_left(asort, a[i])
        ans[i] = num * diff
        for j in range(place, len(keys)):
            if keys[j] <= max_:
                continue
            elif keys[j] >= a[i]:
                place = j
                break
            else:
                ans[i] += (keys[j] - max_) * d[keys[j]]
        max_ = a[i]

ans[0] = sum(a) - sum(ans[1:])

for i in range(N):
    print(ans[i])
