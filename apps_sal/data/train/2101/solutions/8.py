from collections import Counter as CO
import sys
input = sys.stdin.readline


def find(parent, x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent, parent[x])
        return parent[x]


def union(parent, x, y, member):
    parent[x] = find(parent, x)
    parent[y] = find(parent, y)
    if parent[x] == parent[y]:
        return
    else:
        if x < y:
            (x, y) = (y, x)
        member[parent[y]] += member[parent[x]]
        del member[parent[x]]
        parent[parent[x]] = parent[y]
        return


(n, m) = list(map(int, input().split()))
graph = dict()
for i in range(1, n + 1):
    graph[i] = []
for i in range(m):
    (a, b) = list(map(int, input().split()))
    if b > a:
        (a, b) = (b, a)
    graph[a] += [b]
count = 0
parent = dict()
member = dict()
for i in range(1, n + 1):
    parent[i] = i
for i in range(1, n + 1):
    l = []
    for r in graph[i]:
        l += [find(parent, r)]
    d = dict(CO(l))
    x = [j for j in member]
    member[i] = 1
    for k in x:
        if k not in d:
            union(parent, i, k, member)
        elif d[k] < member[k]:
            union(parent, i, k, member)
print(len(member) - 1)
