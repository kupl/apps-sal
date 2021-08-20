import sys
N = int(input())
edge = [list(map(int, input().split())) for i in range(N - 1)]
inf = 10 ** 20
c = [[] for i in range(N)]
for (i, j) in edge:
    c[i - 1].append(j - 1)
    c[j - 1].append(i - 1)
d = [0] + [inf] * (N - 1)
v = [0] * N
sys.setrecursionlimit(10 ** 6)


def dfs(p, v, d):
    for n in c[p]:
        if v[n] == 0:
            d[n] = min(d[n], d[p] + 1)
            v[n] = 1
            dfs(n, v, d)


dfs(0, v, d)
d2 = [inf] * (N - 1) + [0]
v = [0] * N
dfs(N - 1, v, d2)
c = 0
for (i, j) in zip(d, d2):
    c = c + 1 if i <= j else c - 1
print(['Snuke', 'Fennec'][c > 0])
