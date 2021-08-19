from collections import defaultdict as dd
from collections import deque
import bisect
import heapq


def ri():
    return int(input())


def rl():
    return list(map(int, input().split()))


def solve():
    n = ri()
    output = [0] * n
    Q = [(-n, 0, n - 1)]
    for i in range(1, n + 1):
        prev = heapq.heappop(Q)
        (lo, hi) = (prev[1], prev[2])
        mid = (lo + hi) // 2
        output[mid] = i
        if mid > lo:
            heapq.heappush(Q, (-(mid - 1 - lo), lo, mid - 1))
        if hi > mid:
            heapq.heappush(Q, (-(hi - 1 - mid), mid + 1, hi))
    print(*output)


mode = 'T'
if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
