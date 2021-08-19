def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def unite(x, y):
    p = find(x)
    q = find(y)
    if p == q:
        return None
    if p > q:
        (p, q) = (q, p)
    par[p] += par[q]
    par[q] = p


def same(x, y):
    return find(x) == find(y)


def size(x):
    return -par[find(x)]


(n, m) = map(int, input().split())
par = [-1 for i in range(n)]
p = list(map(int, input().split()))
for i in range(m):
    (x, y) = map(int, input().split())
    unite(x - 1, y - 1)
ans = 0
for i in range(n):
    if same(p[i] - 1, i):
        ans += 1
print(ans)
