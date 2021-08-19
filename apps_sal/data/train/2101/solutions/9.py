from collections import defaultdict as dd
import sys
input = sys.stdin.readline


def find(parent, x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent, parent[x])
        return parent[x]


def union(x, y, parent):
    parent[x] = find(parent, x)
    parent[y] = find(parent, y)
    if parent[x] == parent[y]:
        return
    else:
        parent[parent[y]] = parent[x]


(n, m) = map(int, input().split())
d = dd(list)
for i in range(m):
    (u, v) = map(int, input().split())
    if u > v:
        (u, v) = (v, u)
    d[v].append(u)
parent = dd(int)
com = dd(int)
com[1] = 1
for i in range(1, n + 1):
    parent[i] = i
com[1] = 1
for i in range(2, n + 1):
    co = dd(int)
    for j in com:
        co[j] = 0
    for j in d[i]:
        a = find(parent, j)
        co[a] += 1
    x = dd(int)
    for j in com:
        x[j] = com[j]
    lol = 0
    com[i] = 1
    for j in x:
        if co[j] < com[j]:
            a = find(parent, i)
            union(j, i, parent)
            com[j] += com[a]
            del com[a]
            lol = 1
print(len(com) - 1)
