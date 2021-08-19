import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    (n, m) = map(int, input().split())
    s = [input() for i in range(n)]
    grid = [input() for i in range(n)]
    robot_cnt = 0
    black_cnt = 0
    graph = [-1] * (n * m)
    rev_graph = [[] for i in range(n * m)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'U':
                graph[i * m + j] = (i - 1) * m + j
                rev_graph[(i - 1) * m + j].append(i * m + j)
            elif grid[i][j] == 'R':
                graph[i * m + j] = i * m + (j + 1)
                rev_graph[i * m + (j + 1)].append(i * m + j)
            elif grid[i][j] == 'D':
                graph[i * m + j] = (i + 1) * m + j
                rev_graph[(i + 1) * m + j].append(i * m + j)
            elif grid[i][j] == 'L':
                graph[i * m + j] = i * m + (j - 1)
                rev_graph[i * m + (j - 1)].append(i * m + j)
    is_start = [True] * (n * m)
    for i in graph:
        is_start[i] = False
    is_cycle = [False] * (n * m)
    period = [0] * (n * m)
    for i in range(n * m):
        if not is_start[i]:
            continue
        st = i
        period[i] = 1
        while True:
            nxt_i = graph[i]
            if period[nxt_i] < 0:
                tmp = period[nxt_i]
                break
            if period[nxt_i] > 0:
                tmp = -(period[i] - period[nxt_i] + 1)
                is_cycle[nxt_i] = True
                break
            period[graph[i]] = period[i] + 1
            i = graph[i]
        i = st
        period[i] = tmp
        while True:
            nxt_i = graph[i]
            if period[nxt_i] < 0:
                break
            period[graph[i]] = tmp
            i = graph[i]
    for i in range(n * m):
        if period[i] == 0:
            robot_cnt += 1
            if s[i // m][i % m] == '0':
                black_cnt += 1
    for i in range(n * m):
        if not is_cycle[i]:
            continue
        MOD = -period[i]
        period[i] = 0
        is_black = [False] * MOD
        if s[i // m][i % m] == '0':
            is_black[0] = True
        q = deque([i])
        while q:
            v = q.pop()
            for nxt_v in rev_graph[v]:
                if period[nxt_v] >= 0:
                    continue
                period[nxt_v] = (period[v] + 1) % MOD
                if s[nxt_v // m][nxt_v % m] == '0':
                    is_black[period[nxt_v]] = True
                q.append(nxt_v)
        robot_cnt += MOD
        black_cnt += sum(is_black)
    print(robot_cnt, black_cnt)
