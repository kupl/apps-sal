import sys
from collections import deque
input = sys.stdin.readline
N, M = list(map(int, input().split()))
c, to = dict(), [[] for _ in range(N)]


def maxmin(x, y):
    if x < y:
        x, y = y, x
    return (x, y)


for i in range(M):
    x, y, z = list(map(int, input().split()))
    x, y = x - 1, y - 1
    x, y = maxmin(x, y)
    c[(x, y)] = z
    to[x].append(y)
    to[y].append(x)

d = deque()
d.append(0)
seen = [False] * N
seen[0] = True
mark = [1] * N
while len(d) > 0:
    now = d.popleft()
    for next in to[now]:
        if seen[next]:
            continue
        seen[next] = True
        d.append(next)
        xy = maxmin(next, now)
        if mark[now] == c[xy]:
            mark[next] = (mark[now] % N) + 1
        else:
            mark[next] = c[xy]

for i in mark:
    print(i)
