n, m = map(int, input().split())
p = [int(i)for i in input().split()]
par = [i for i in range(n)]


def find(x):
    if x == par[x]:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def unite(x, y):
    x, y = find(x), find(y)
    if x > y:
        x, y = y, x
    if x != y:
        par[y] = x


for _ in range(m):
    a, b = map(int, input().split())
    unite(a - 1, b - 1)
for i in range(n):
    find(i)
print(sum(find(i) == find(p[i] - 1)for i in range(n)))
