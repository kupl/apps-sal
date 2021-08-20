def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]


def merge(a, b):
    (a, b) = (find(a), find(b))
    if rank[a] > rank[b]:
        parent[b] = a
        size[a] += size[b]
    else:
        parent[a] = b
        size[b] += size[a]
        if rank[a] == rank[b]:
            rank[b] += 1


n = int(input())
size = {}
rank = {}
parent = {}
edges = []
for i in range(n):
    size[i] = 1
    parent[i] = i
    rank[i] = 1
for i in range(n - 1):
    (a, b, c) = list(map(int, input().split()))
    a -= 1
    b -= 1
    edges.append([c, a, b])
edges.sort()
S = T = C = 0
for (c, a, b) in edges:
    a = find(a)
    b = find(b)
    S += size[a] * size[b] * c
    T += size[a] * size[b]
    C += c
    merge(a, b)
print(C - S / T)
