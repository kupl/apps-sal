def issafe(r, c, r1, c1, graph, n, m):
    if r > -1 and r1 > -1 and (c > -1) and (c1 > -1) and (r < n) and (r1 < n) and (c < m) and (c1 < m) and graph[r][c] and graph[r1][c1]:
        return True
    return False


t = int(input())
for mmmmmm in range(t):
    (n, m) = map(int, input().split())
    (x, y) = map(int, input().split())
    graph = [[False] * m for _ in range(n)]
    cost_graph = [[[-1, -1, -1] for __ in range(m)] for _ in range(n)]
    for i in range(n):
        str1 = input()
        for (j, val) in enumerate(str1):
            graph[i][j] = val == '1'
    x = x - 1
    y = y - 1
    set1 = set()
    set1.add((x, y, 0))
    cost_graph[x][y][0] = 0
    while set1:
        set2 = set()
        while set1:
            (r, c, p) = set1.pop()
            new_cost = cost_graph[r][c][p] + 1
            if p == 0:
                if issafe(r, c + 1, r, c + 2, graph, n, m):
                    if cost_graph[r][c + 1][1] == -1 or cost_graph[r][c + 1][1] > new_cost:
                        cost_graph[r][c + 1][1] = new_cost
                        set2.add((r, c + 1, 1))
                if issafe(r + 1, c, r + 2, c, graph, n, m):
                    if cost_graph[r + 1][c][2] == -1 or cost_graph[r + 1][c][2] > new_cost:
                        cost_graph[r + 1][c][2] = new_cost
                        set2.add((r + 1, c, 2))
                if issafe(r, c - 2, r, c - 1, graph, n, m):
                    if cost_graph[r][c - 2][1] == -1 or cost_graph[r][c - 2][1] > new_cost:
                        cost_graph[r][c - 2][1] = new_cost
                        set2.add((r, c - 2, 1))
                if issafe(r - 2, c, r - 1, c, graph, n, m):
                    if cost_graph[r - 2][c][2] == -1 or cost_graph[r - 2][c][2] > new_cost:
                        cost_graph[r - 2][c][2] = new_cost
                        set2.add((r - 2, c, 2))
            elif p == 1:
                if issafe(r, c + 2, r, c + 2, graph, n, m):
                    if cost_graph[r][c + 2][0] == -1 or cost_graph[r][c + 2][0] > new_cost:
                        cost_graph[r][c + 2][0] = new_cost
                        set2.add((r, c + 2, 0))
                if issafe(r + 1, c, r + 1, c + 1, graph, n, m):
                    if cost_graph[r + 1][c][1] == -1 or cost_graph[r + 1][c][1] > new_cost:
                        cost_graph[r + 1][c][1] = new_cost
                        set2.add((r + 1, c, 1))
                if issafe(r, c - 1, r, c - 1, graph, n, m):
                    if cost_graph[r][c - 1][0] == -1 or cost_graph[r][c - 1][0] > new_cost:
                        cost_graph[r][c - 1][0] = new_cost
                        set2.add((r, c - 1, 0))
                if issafe(r - 1, c, r - 1, c + 1, graph, n, m):
                    if cost_graph[r - 1][c][1] == -1 or cost_graph[r - 1][c][1] > new_cost:
                        cost_graph[r - 1][c][1] = new_cost
                        set2.add((r - 1, c, 1))
            elif p == 2:
                if issafe(r, c + 1, r + 1, c + 1, graph, n, m):
                    if cost_graph[r][c + 1][2] == -1 or cost_graph[r][c + 1][2] > new_cost:
                        cost_graph[r][c + 1][2] = new_cost
                        set2.add((r, c + 1, 2))
                if issafe(r + 2, c, r + 2, c, graph, n, m):
                    if cost_graph[r + 2][c][0] == -1 or cost_graph[r + 2][c][0] > new_cost:
                        cost_graph[r + 2][c][0] = new_cost
                        set2.add((r + 2, c, 0))
                if issafe(r, c - 1, r + 1, c - 1, graph, n, m):
                    if cost_graph[r][c - 1][2] == -1 or cost_graph[r][c - 1][2] > new_cost:
                        cost_graph[r][c - 1][2] = new_cost
                        set2.add((r, c - 1, 2))
                if issafe(r - 1, c, r - 1, c, graph, n, m):
                    if cost_graph[r - 1][c][0] == -1 or cost_graph[r - 1][c][0] > new_cost:
                        cost_graph[r - 1][c][0] = new_cost
                        set2.add((r - 1, c, 0))
        set1 = set2
    for _ in range(n):
        for __ in range(m):
            print(cost_graph[_][__][0], end=' ')
        print()
