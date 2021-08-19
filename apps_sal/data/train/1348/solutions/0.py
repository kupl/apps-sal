from collections import defaultdict
import copy


def dfs(l, r, dct):
    visit = [0 for i in range(n + 1)]
    arr = [l]
    while arr:
        node = arr.pop()
        if node == r:
            return True
        visit[node] = 1
        for lnk in dct[node]:
            if not visit[lnk]:
                arr.append(lnk)
    return False


def ok(mid, cst):
    for (i, j) in edges:
        cst[i][j] -= mid
    d = [10 ** 9] * (n + 1)
    d[l] = 0
    for _ in range(n - 1):
        for (i, j) in edges:
            d[j] = min(d[j], d[i] + cst[i][j])
    if d[r] <= 0:
        return 1
    for (i, j) in edges:
        if d[j] > d[i] + cst[i][j] and dfs(l, i, dct) and dfs(j, r, dct):
            return 1
    return 0


for _ in range(int(input())):
    (n, m) = map(int, input().split())
    dct = defaultdict(list)
    cost = [[1000 for i in range(n + 1)] for j in range(n + 1)]
    edges = []
    for i in range(m):
        (a, b, w) = map(int, input().split())
        edges.append([a, b])
        dct[a].append(b)
        cost[a][b] = min(cost[a][b], w)
    (l, r) = map(int, input().split())
    if not dfs(l, r, dct):
        print(-1)
        continue
    lo = 1
    hi = 101
    for i in range(100):
        cst = copy.deepcopy(cost)
        mid = (lo + hi) / 2
        if ok(mid, cst):
            hi = mid - 1
        else:
            lo = mid + 1
    print('%.7f' % mid)
