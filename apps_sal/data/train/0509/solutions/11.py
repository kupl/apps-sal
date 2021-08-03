from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

N, M, *UVC = map(int, open(0).read().split())

E = [[] for _ in range(N + 1)]
for u, v, c in zip(*[iter(UVC)] * 3):
    E[u].append((v, c))
    E[v].append((u, c))

memo = [-1] * (N + 1)
memo[1] = 1


def dfs(cur, par):
    for nxt, c in E[cur]:
        if memo[nxt] != -1 or nxt == par:
            continue
        if memo[cur] == c:
            c = 1 + (c == 1)
        memo[nxt] = c
        dfs(nxt, cur)


dfs(1, 0)

for m in memo[1:]:
    print(m)
