n, m = map(int, input().split())
pn = list(map(lambda x: int(x) - 1, input().split()))
ls = [-1] * n
for i in pn:
    ls[pn[i]] = i

par = [i for i in range(n)]


def find(x):
    if par[x] == x:
        return x
    else:
        s = find(par[x])
        par[x] = s
        return s


def unite(x, y):
    s = find(x)
    t = find(y)
    if s > t:
        par[s] = t
    else:
        par[t] = s


for _ in range(m):
    x, y = map(lambda x: int(x) - 1, input().split())
    unite(ls[x], ls[y])

dic = {}
for i in range(n):
    a = find(i)
    if a in dic:
        dic[a].add(ls[i])
    else:
        dic[a] = set([ls[i]])
ans = 0
for i in range(n):
    if i in dic[find(i)]:
        ans += 1
print(ans)
