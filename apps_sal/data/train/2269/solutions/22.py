from collections import deque


n, m = map(int, input().split())
info = [list(map(int, input().split())) for i in range(m)]

matrix = [[0] * n for i in range(n)]
for i in range(m):
    a, b = info[i]
    a -= 1
    b -= 1
    matrix[a][b] = 1
    matrix[b][a] = 1

graph = [[] for i in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] == 0:
            graph[i].append(j)
            graph[j].append(i)


def coloring(graph):
    n = len(graph)
    visited = [-1] * n
    ans = []
    for i in range(n):
        if visited[i] >= 0:
            continue
        visited[i] = 0
        q = deque([i])
        num = [1, 0]
        while q:
            _from = q.pop()
            for to in graph[_from]:
                if visited[to] == visited[_from]:
                    return [[-1, -1]]
                if visited[to] >= 0:
                    continue
                visited[to] = visited[_from] ^ 1
                num[visited[to]] += 1
                q.append(to)
        ans.append(num)
    return ans


num = coloring(graph)
if num[0][0] == -1:
    print(-1)
    return

dp = [[False] * (n + 1) for _ in range(len(num) + 1)]
dp[0][0] = True

for i in range(len(num)):
    a, b = num[i]
    for j in range(n + 1):
        if j - a >= 0:
            dp[i + 1][j] = dp[i][j - a] or dp[i + 1][j]
        if j - b >= 0:
            dp[i + 1][j] = dp[i][j - b] or dp[i + 1][j]

ans = 10**20
for i, boolian in enumerate(dp[len(num)]):
    if boolian:
        tmp_ans = i * (i - 1) // 2 + (n - i) * (n - i - 1) // 2
        ans = min(tmp_ans, ans)
print(ans)
