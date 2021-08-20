import numpy as np
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
(N, Q) = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    (a, b, c, d) = map(int, input().split())
    graph[a].append((b, c, d))
    graph[b].append((a, c, d))
query = [[int(x) for x in input().split()] for _ in range(Q)]


def euler_tour(x, tour_v, tour_d, depth=0, parent=None):
    tour_v.append(x)
    tour_d.append(depth)
    for (y, c, d) in graph[x]:
        if y == parent:
            continue
        euler_tour(y, tour_v, tour_d, depth + 1, parent=x)
        tour_v.append(x)
        tour_d.append(depth)


tour_v = []
tour_d = []
euler_tour(1, tour_v, tour_d)
tour_d_arr = np.array(tour_d)
v_to_i = {v: i for (i, v) in enumerate(tour_v)}
v_to_d = dict(zip(tour_v, tour_d))
L = len(tour_v)
U = L.bit_length()
sp = [np.arange(L)]
for i in range(1, U):
    prev = sp[-1]
    width = 1 << i - 1
    n1 = prev[:-width]
    n2 = prev[width:]
    sp.append(np.where(tour_d_arr[n1] < tour_d_arr[n2], n1, n2))


def LCA(x, y):
    ix = v_to_i[x]
    iy = v_to_i[y]
    if ix > iy:
        (ix, iy) = (iy, ix)
    items = iy - ix + 1
    L = items.bit_length() - 1
    n1 = sp[L][ix]
    n2 = sp[L][iy - (1 << L) + 1]
    n = n1 if tour_d[n1] < tour_d[n2] else n2
    return tour_v[n]


tasks = [[] for _ in range(N + 1)]
for (i, (x, y, u, v)) in enumerate(query):
    tasks[u].append((i, x, y, 1))
    tasks[v].append((i, x, y, 1))
    tasks[LCA(u, v)].append((i, x, y, -2))
answer = [0] * Q


def dfs(x=1, sums=[0] * (N + 1), nums=[0] * (N + 1), total=0, parent=0):
    for (i, c, d, coef) in tasks[x]:
        answer[i] += coef * (total - sums[c] + nums[c] * d)
    for (y, c, d) in graph[x]:
        if y == parent:
            continue
        sums[c] += d
        nums[c] += 1
        total += d
        dfs(y, sums, nums, total, x)
        sums[c] -= d
        nums[c] -= 1
        total -= d
    return


dfs()
print('\n'.join(map(str, answer)))
