from collections import deque
import sys


def int1(x):
    return int(x) - 1


def p2D(x):
    return print(*x, sep='\n')


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def MI1():
    return map(int1, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def SI():
    return sys.stdin.readline()[:-1]


def solve():
    dist = [inf] * len(to)
    q = deque()
    q.append((0, 0))
    dist[0] = 0
    while q:
        (d, i) = q.popleft()
        if d > dist[i]:
            continue
        if i < n:
            for j in to[i]:
                if dist[j] <= d + 1:
                    continue
                dist[j] = d + 1
                q.append((d + 1, j))
        else:
            for j in to[i]:
                if j == n - 1:
                    print(dist[i])
                    return
                if dist[j] <= d:
                    continue
                dist[j] = d
                q.appendleft((d, j))
    print(-1)


inf = 10 ** 9
(n, m) = MI()
to = []
uctoi = {}
for u in range(n):
    to.append([])
    uctoi[u, 0] = u
for _ in range(m):
    (u, v, c) = MI()
    (u, v) = (u - 1, v - 1)
    if (u, c) not in uctoi:
        i = uctoi[u, c] = len(to)
        to.append([])
        to[i].append(u)
        to[u].append(i)
    else:
        i = uctoi[u, c]
    if (v, c) not in uctoi:
        j = uctoi[v, c] = len(to)
        to.append([])
        to[j].append(v)
        to[v].append(j)
    else:
        j = uctoi[v, c]
    to[i].append(j)
    to[j].append(i)
solve()
