from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 8)
inf = 10 ** 10
n = int(input())
l = [[] for i in range(n + 1)]
for i in range(n - 1):
    (a, b) = map(int, input().split())
    l[a].append(b)
    l[b].append(a)
prev = [-1 for i in range(n + 1)]


def dijkstra(s):
    q = [(0, s)]
    dist = [inf] * (n + 1)
    dist[s] = 0
    while q:
        (c, v) = heappop(q)
        if dist[v] < c:
            continue
        for i in l[v]:
            t = i
            cost = 1
            if dist[v] + cost < dist[t]:
                dist[t] = dist[v] + cost
                prev[t] = v
                heappush(q, [dist[t], t])
    return dist


d = dijkstra(1)
p = [n]
num = n
next = [-1 for i in range(n + 1)]
while num != 1:
    num1 = prev[num]
    next[num1] = num
    p.append(num1)
    num = num1
countp = [0]
countf = [0]


def dfs(x, y):
    for i in l[x]:
        if prev[x] != i and next[x] != i:
            if y == 1:
                countp[0] += 1
            else:
                countf[0] += 1
            prev[i] = x
            dfs(i, y)


p = p[::-1]
num = len(p)
num1 = (num - 1) // 2 + 1
for i in range(num1):
    countp[0] += 1
    dfs(p[i], 1)
for i in range(num1, num):
    countf[0] += 1
    dfs(p[i], 0)
if countp[0] > countf[0]:
    print('Fennec')
else:
    print('Snuke')
