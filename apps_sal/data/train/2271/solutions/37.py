def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])  # 経路圧縮
        return par[x]


def same(x, y):
    return find(x) == find(y)


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[x] = y
    size[y] = size[x] + size[y]
    size[x] = 0


N, M = list(map(int, input().split()))
plist = list(map(int, input().split()))
ABs = [list(map(int, input().split())) for _ in range(M)]
par = [i for i in range(N + 1)]
size = [1 for _ in range(N + 1)]

for AB in ABs:
    unite(AB[0], AB[1])

Ans = 0
for i in range(len(plist)):
    if plist[i] == i + 1:
        Ans += 1
    else:
        if same(plist[i], i + 1):
            Ans += 1
print(Ans)
