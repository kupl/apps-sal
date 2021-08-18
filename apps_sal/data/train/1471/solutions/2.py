from queue import Queue


def run_bfs(x, y, k1, a):
    visited = []
    n = len(a)
    m = len(a[0])
    inf = float("inf")
    for i in range(0, n):
        visited = visited + [[inf] * m]
    visited[x][y] = 0
    qu = Queue()
    qu.put((x, y, 0))
    while(not(qu.empty())):
        (x1, y1, a1) = qu.get()
        for x_n in range(max(x1 - k1, 0), min(x1 + k1 + 1, n)):
            t1 = abs(x_n - x1)
            for y_n in range(max(y1 - k1 + t1, 0), min(y1 + k1 - t1 + 1, m)):
                if (a[x_n][y_n] == 0):
                    if (visited[x_n][y_n] == inf):
                        visited[x_n][y_n] = a1 + 1
                        qu.put((x_n, y_n, a1 + 1))
    return visited


t = eval(input())
for i in range(0, t):
    inp = input()
    inp = [int(j) for j in inp.split()]
    [n, m, k1, k2] = inp
    a = []
    for t1 in range(0, n):
        inp = input()
        inp = [int(j) for j in inp.split()]
        a = a + [inp]
    visited1 = run_bfs(0, 0, k1, a)
    visited2 = run_bfs(0, m - 1, k2, a)
    m1 = float("inf")
    for x in range(0, n):
        for y in range(0, m):
            m_l = max(visited1[x][y], visited2[x][y])
            m1 = min(m_l, m1)
    if (m1 < float("inf")):
        print(m1)
    else:
        print("-1")
