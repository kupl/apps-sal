n = int(input())
pos, tree, ans, sz = list(map(int, input().split())) if n > 1 else [], [], [], []
for i in range(n):
    tree.append([])
    ans.append(0.0)
    sz.append(0)

for i in range(n - 1):
    tree[pos[i] - 1].append(i + 1)

for i in range(n)[::-1]:
    sz[i] = 1
    for to in tree[i]:
        sz[i] += sz[to]

for i in range(n):
    for to in tree[i]:
        ans[to] = ans[i] + 1 + (sz[i] - 1 - sz[to]) * 0.5


def st(i): return str(i + 1)


print(' '.join(list(map(st, ans))))
