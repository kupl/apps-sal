n, m = map(int, input().split())
p = [[0]] + [[int(i)]for i in input().split()]
q = [[i]for i in range(n + 1)]
par = [i for i in range(n + 1)]


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
        p[x] += p[y]
        q[x] += q[y]


for _ in range(m):
    a, b = map(int, input().split())
    unite(a, b)
for i in range(n):
    find(i)
ans = -1
for i in set(par):
    ans += len(set(p[i]) & set(q[i]))
print(ans)
