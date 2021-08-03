n, k = list(map(int, input().split()))
parent = [i for i in range(n)]
rank = [1 for i in range(n)]


def find_parent(u):
    if parent[u] != u:
        parent[u] = find_parent(parent[u])
    return parent[u]


for i in range(k):
    u, v = list(map(int, input().split()))
    u = find_parent(u - 1)
    v = find_parent(v - 1)
    if u != v:
        parent[u] = v
        rank[v] += rank[u]
sat = 0
for i in range(n):
    if parent[i] == i:
        sat += (rank[i] - 1)
print(k - sat)
