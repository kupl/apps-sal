from collections import Counter, deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
E = [list(map(int, input().split())) for i in range(m)]

F = []

# E = [(cost, v, w), ...]
#   G上の全ての辺(v, w)とそのcostを含むlist

# Union-Findを使うことで頂点間の連結判定を行う

*p, = range(n)


def root(x):
    if x == p[x]:
        return x
    p[x] = y = root(p[x])
    return y


def unite(x, y):
    px = root(x)
    py = root(y)
    if px == py:
        return 0
    if px < py:
        p[py] = px
    else:
        p[px] = py
    return 1


E.sort()
ans = 0
for v, w, c in E:
    if unite(v - 1, w - 1):
        F.append([v, w, c])
        ans += c

# ansが最小全域木の解

g = [[] for i in range(n)]
ans = [0] * n
ans[0] = '?'
used = [False] * (n + 1)
pre = [0] * n

for u, v, c in F:
    g[u - 1].append([v - 1, c])
    g[v - 1].append([u - 1, c])


Q = deque()
Q.append((0))

while Q:
    p = Q.popleft()

    for s in g[p]:
        i, v = s[0], s[1]
        if ans[i] == 0:
            if ans[p] == v:
                ans[i] = v + 1
                Q.append((i))
                if ans[i] == n + 1:
                    ans[i] = 1
            else:
                ans[i] = v
                Q.append((i))


for i, v in g[0]:
    used[v] = True

for i in range(1, n + 1):
    if used[i] == False:
        ans[0] = i
        break


print(*ans, sep='\n')
