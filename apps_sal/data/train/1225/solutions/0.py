t = eval(input())


def func(k, n, x, dist, graph):
    if k == n:
        x += [dist[n]]
        return
    for i in range(1, n + 1):
        if graph[k][i] != 0 and dist[i] == -1:
            dist[i] = dist[k] + graph[k][i]
            func(i, n, x, dist, graph)
            dist[i] = -1


while t:
    graph = [[0 for i in range(11)]for j in range(11)]
    v, e = list(map(int, input().split()))
    for i in range(e):
        x, y, w = list(map(int, input().split()))
        graph[x][y] = w
        graph[y][x] = w
    x = []
    dist = [-1] * (v + 1)
    dist[1] = 0
    func(1, v, x, dist, graph)
    x.sort()
    val = x[0]
    ans = 0
    for i in range(len(x)):
        if val == x[i]:
            ans += 1
    print(ans)
    t -= 1
