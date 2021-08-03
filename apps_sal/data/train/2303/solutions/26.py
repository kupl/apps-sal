from heapq import heappush, heappop, heappushpop, heapify
from collections import defaultdict
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
link = defaultdict(list)
chg = 10**8
for _ in range(m):
    p, q, c = map(int, input().split())
    link[p].append([p + chg * c, 1])
    link[p + chg * c].append([p, 1])

    link[q + chg * c].append([p + chg * c, 0])
    link[p + chg * c].append([q + chg * c, 0])

    link[q + chg * c].append([q, 1])
    link[q].append([q + chg * c, 1])


def dks(g, start):
    INF = float('inf')
    visited = set()
    hq = []
    heappush(hq, (0, start))
    while hq:
        shortest, i = heappop(hq)
        if i in visited:
            continue
        visited.add(i)
        for j, t in g[i]:
            if j in visited:
                continue
            if j == n:
                return (shortest + t) // 2
            heappush(hq, (shortest + t, j))
    return -1


ans = dks(link, 1)
print(ans)
