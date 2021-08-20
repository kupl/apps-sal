import sys
input = sys.stdin.readline


def I():
    return list(map(int, input().split()))


sys.setrecursionlimit(10 ** 5)
(n, m) = I()
g = [set() for i in range(n)]
for i in range(m):
    (u, v) = I()
    g[u - 1].add(v - 1)
    g[v - 1].add(u - 1)
p = [i for i in range(n)]


def find(x):
    while x != p[x]:
        x = p[x]
    return x


def union(a, b):
    x = find(a)
    y = find(b)
    p[y] = x


for i in range(n):
    if p[i] == i:
        for j in range(n):
            if j not in g[i]:
                g[i] &= g[j]
        for j in range(n):
            if j not in g[i]:
                union(i, j)
print(len(set([find(i) for i in range(n)])) - 1)
