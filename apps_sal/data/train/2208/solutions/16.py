def find_set(v):
    if v == parent[v]:
        return v
    parent[v] = find_set(parent[v])
    return parent[v]


def union_sets(x, y):
    x = find_set(x)
    y = find_set(y)
    if x != y:
        if rank[x] < rank[y]:
            x, y = y, x
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


n, k = list(map(int, input().split()))
parent = [0] * n
rank = [0] * n
vis = [0] * n
for i in range(n):
    parent[i] = i
for _ in range(k):
    x, y = list(map(int, input().split()))
    union_sets(x - 1, y - 1)
    # print(parent)

c = 0
for i in range(n):
    if parent[i] == i:
        c += 1
print(k - n + c)
