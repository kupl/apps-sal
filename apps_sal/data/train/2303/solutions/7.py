import sys
import heapq
from collections import defaultdict, deque

input = sys.stdin.readline
n, m = map(int, input().split())
# +路線*chg : その路線ホーム
chg = 10**6

edge = defaultdict(set)
used = defaultdict(bool)
for i in range(m):
    p, q, c = map(int, input().split())
    edge[p].add(p + c * chg)
    edge[p + c * chg].add(p)
    edge[p + c * chg].add(q + c * chg)
    edge[q + c * chg].add(p + c * chg)
    edge[q].add(q + c * chg)
    edge[q + c * chg].add(q)
    used[p] = False
    used[q] = False
    used[p + c * chg] = False
    used[q + c * chg] = False

edgelist = deque()
edgelist.append((1, 0))
res = float("inf")

while len(edgelist):
    x, cost = edgelist.pop()
    used[x] = True

    if x == n:
        res = cost
        break
    for e in edge[x]:
        if used[e]:
            continue
        # ホーム→改札
        if x <= 10**5 and chg <= e:
            edgelist.appendleft((e, cost + 1))
        else:
            edgelist.append((e, cost))

if res == float("inf"):
    print(-1)
else:
    print(res)
