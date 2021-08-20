p = 998244353
n = int(input())
facs = [1]
for i in range(1, n):
    facs.append(facs[-1] * i % p)
graph = [[] for i in range(n)]
for i in range(n - 1):
    (u, v) = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)
prod = facs[len(graph[0])] * n
for i in range(1, n):
    k = len(graph[i])
    prod = prod * facs[k] % p
print(prod)
