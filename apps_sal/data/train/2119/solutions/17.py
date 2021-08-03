import sys

MAX = 100005
arr = MAX * [0]
pre = MAX * [0]
ix = MAX * [0]
sun = MAX * [0]
ans = MAX * [0]
vis = MAX * [False]
mx = 0


def find(x):
    if x == pre[x]:
        return x
    pre[x] = find(pre[x])
    return pre[x]


def unite(x, y):

    dx = find(x)
    dy = find(y)
    if dx == dy:
        return
    pre[dx] = dy
    sun[dy] += sun[dx]


n = int(input())
arr = [int(i) for i in input().split()]
arr.insert(0, 0)
sun = arr
pre = [i for i in range(n + 1)]
ix = [int(i) for i in input().split()]


for i in range(n - 1, -1, -1):
    x = ix[i]
    ans[i] = mx
    vis[x] = True
    if x != 1 and vis[x - 1]:
        unite(x - 1, x)
    if x != n and vis[x + 1]:
        unite(x, x + 1)
    mx = max(mx, sun[find(x)])

for i in range(n):
    print(ans[i])
