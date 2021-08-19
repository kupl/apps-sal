import sys
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def dijkstra(n, s, cost):
    res = [f_inf] * n
    res[s] = 0
    checked = [False] * n
    while True:
        v = -1
        for k in range(n):
            if not checked[k] and v == -1:
                v = k
            elif not checked[k] and res[k] < res[v]:
                v = k
        if v == -1:
            break
        checked[v] = True
        for m in range(n):
            res[m] = min(res[m], res[v] + cost[v][m])
    return res


def resolve():

    def calc_dist(x1, y1, x2, y2):
        return pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5)
    (sx, sy, gx, gy) = list(map(int, input().split()))
    n = int(input())
    node = [[sx, sy, 0]] + [list(map(int, input().split())) for _ in range(n)] + [[gx, gy, 0]]
    cost = [[0] * (n + 2) for _ in range(n + 2)]
    for i in range(n + 2):
        (x1, y1, r1) = node[i]
        for j in range(i + 1, n + 2):
            (x2, y2, r2) = node[j]
            dist = max(0, calc_dist(x1, y1, x2, y2) - (r1 + r2))
            cost[i][j] = dist
            cost[j][i] = dist
    res = dijkstra(n + 2, 0, cost)
    print(res[-1])


def __starting_point():
    resolve()


__starting_point()
