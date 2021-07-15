N, M = list(map(int,input().split()))
p = list(map(int,input().split()))
parent = [k for k in range(N)]
def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return find(parent[x])
def unite(x,y):
    parent[find(x)] = find(y)

for _ in range(M):
    x, y = list(map(int,input().split()))
    unite(x-1,y-1)
ans = 0
for k in range(N):
    if find(k) == find(p[k]-1):
        ans += 1
print(ans)

